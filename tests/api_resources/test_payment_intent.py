from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'pi_123'


class TestPaymentIntent(object):
    FIXTURE = {
        'id': TEST_RESOURCE_ID,
        'object': 'payment_intent',
        'metadata': {},
    }

    def test_is_listable(self, request_mock):
        request_mock.stub_request(
            'get',
            '/v1/payment_intents',
            {
                'object': 'list',
                'data': [self.FIXTURE],
            }
        )

        resources = stripe.PaymentIntent.list()
        request_mock.assert_requested(
            'get',
            '/v1/payment_intents'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PaymentIntent)

    def test_is_retrievable(self, request_mock):
        request_mock.stub_request(
            'get',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_creatable(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/payment_intents',
            self.FIXTURE
        )

        resource = stripe.PaymentIntent.create(
            allowed_source_types=['card'],
            amount='1234',
            currency='amount'
        )
        request_mock.assert_requested(
            'post',
            '/v1/payment_intents',
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_modifiable(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource = stripe.PaymentIntent.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            {'metadata': {'key': 'value'}}
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_saveable(self, request_mock):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        request_mock.stub_request(
            'post',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/payment_intents/%s' % resource.id,
            {'metadata': {'key': 'value'}}
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_cancel(self, request_mock):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        request_mock.stub_request(
            'post',
            '/v1/payment_intents/%s/cancel' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.cancel()
        request_mock.assert_requested(
            'post',
            '/v1/payment_intents/%s/cancel' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_capture(self, request_mock):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        request_mock.stub_request(
            'post',
            '/v1/payment_intents/%s/capture' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.capture()
        request_mock.assert_requested(
            'post',
            '/v1/payment_intents/%s/capture' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_confirm(self, request_mock):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        request_mock.stub_request(
            'post',
            '/v1/payment_intents/%s/confirm' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.confirm()
        request_mock.assert_requested(
            'post',
            '/v1/payment_intents/%s/confirm' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)
