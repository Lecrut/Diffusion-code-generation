MIN_MEMBERSHIP_DURATION = 12
MIN_PURCHASE_AMOUNT = 500

def is_eligible_for_discount(membership_duration, purchase_amount):
    return membership_duration >= MIN_MEMBERSHIP_DURATION or purchase_amount > MIN_PURCHASE_AMOUNT
if __name__ == '__main__':
    membership_duration = 15
    purchase_amount = 400
    discount_eligible = is_eligible_for_discount(membership_duration, purchase_amount)
    print(f'User is eligible for a discount: {discount_eligible}')