class DiscountEvaluator:
    MIN_PURCHASE = 100
    IS_ELIGIBLE_MEMBERSHIP = True

    @staticmethod
    def is_eligible_for_discount(membership_status, purchase_amount):
        return (membership_status == DiscountEvaluator.IS_ELIGIBLE_MEMBERSHIP) and (purchase_amount >= DiscountEvaluator.MIN_PURCHASE)

if __name__ == '__main__':
    print("--- Testing Discount Eligibility ---")
    membership = True
    amount_spent = 150
    result = DiscountEvaluator.is_eligible_for_discount(membership, amount_spent)
    print(f"Test Case (membership={membership}, amount_spent={amount_spent}): Result = {result}")