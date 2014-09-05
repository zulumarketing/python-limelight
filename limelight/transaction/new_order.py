# -*- coding: utf-8 -*-

from voluptuous import Required, Optional, All, Length, Any

from ..request import TransactionMethod
from ..validation_functions import (country_code, email_address, credit_card_number,
                                    expiration_date, accepted_payment_type, ip_address,
                                    bool_to_one_or_zero, bool_to_yes_or_no)


class NewOrder(TransactionMethod):
    __name__ = 'NewOrder'
    schema = {Required('first_name'): All(str, Length(max=64)),
              Required('last_name'): All(str, Length(max=64)),
              Required('shipping_address1'): All(str, Length(max=64)),
              Optional('shipping_address2'): All(str, Length(max=64)),
              Required('shipping_city'): All(str, Length(max=32)),
              Required('shipping_state'): All(str, Length(max=32)),
              Required('shipping_zip'): All(Any(str, int), lambda shipping_zip: str(shipping_zip),
                                            Length(max=10)),
              Required('shipping_country'): All(str, country_code, Length(2)),
              Required('billing_first_name'): All(str, Length(min=1, max=64)),
              Optional('billing_last_name'): All(str, Length(min=1, max=64)),
              Optional('billing_address1'): All(str, Length(min=1, max=64)),
              Optional('billing_address2'): All(str, Length(min=1, max=64)),
              Optional('billing_city'): All(str, Length(max=32)),
              Optional('billing_state'): All(str, Length(max=32)),
              Optional('billing_zip'): All(Any(str, int), lambda billing_zip: str(billing_zip),
                                           Length(max=10)),
              Optional('billing_country'): All(str, country_code, Length(2)),
              Required('phone'): All(Any(str, int), Length(max=18)),
              Required('email'): All(str, email_address, Length(max=96)),
              Required('credit_card_type'): All(str, accepted_payment_type),
              Required('credit_card_number'): All(str, credit_card_number,
                                                  Length(max=20)),
              Required('expiration_date'): All(expiration_date, Length(4)),
              Required('cvv'): All(int, lambda cvv: str(cvv), Length(min=3, max=4)),
              Required('tran_type'): 'Sale',
              Required('ip_address'): All(str, ip_address, Length(max=15)),
              Optional('AFID'): All(str, Length(max=255)),
              Optional('SID'): All(str, Length(max=255)),
              Optional('AFFID'): All(str, Length(max=255)),
              Optional('C1'): All(str, Length(max=255)),
              Optional('C2'): All(str, Length(max=255)),
              Optional('C3'): All(str, Length(max=255)),
              Optional('AID'): All(str, Length(max=255)),
              Optional('OPT'): All(str, Length(max=255)),
              Optional('click_id'): All(str, Length(max=255)),
              Required('product_id'): int,
              Required('campaign_id'): int,
              Required('shipping_id'): int,
              Required('upsell_count'): All(bool, bool_to_one_or_zero),
              Optional('upsell_product_ids'): [int],
              Optional('billing_same_as_shipping'): All(bool, bool_to_yes_or_no),
              Optional('notes'): All(str, Length(max=512)),
              Optional('preserve_force_gateway'): All(bool, bool_to_one_or_zero),
              Optional('created_by'): All(str, Length(max=100)),
              Optional('thm_session_id'): All(str, Length(max=255)),
              Optional('total_installments'): int,
              Optional('alt_pay_token'): All(str, Length(max=20)),
              Optional('alt_pay_payer_id'): All(str, Length(max=20)),
              Optional('secret_ssn'): All(int, Length(max=4)),
              Optional('force_subscription_cycle'): bool,
              Optional('recurring_days'): int,
              Optional('subscription_week'): Any(1, 2, 3, 4, 5),
              Optional('subscription_day'): Any(1, 2, 3, 4, 5, 6, 7),
              Optional('master_order_id'): int,
              Optional('promo_code'): All(str, Length(max=100)),
              Optional('temp_customer_id'): All(str, Length(max=32)), }