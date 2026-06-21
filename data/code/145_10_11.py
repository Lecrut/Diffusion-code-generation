def is_eligible_for_discount(membership_status, purchase_amount):
    try:
        return (membership_status and purchase_amount >= 100) or (not membership_status and purchase_amount >= 500)
    except TypeError as e:
        print(f"Invalid input: {e}")
        raise

if __name__ == '__main__':
    sample_membership = True
    sample_purchase = 90
    result = is_eligible_for_discount(sample_membership, sample_purchase)
    print(f"User with membership {sample_membership} and purchase ${sample_purchase} is eligible for discount: {result}")