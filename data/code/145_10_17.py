class DiscountEvaluator:
    def __init__(self, is_member=False, purchase_amount=0):
        self.is_member = is_member
        self.purchase_amount = purchase_amount

    def is_eligible_for_discount(self):
        return (self.is_member and self.purchase_amount >= 100) or not self.is_member

if __name__ == '__main__':
    evaluator1 = DiscountEvaluator(True, 50)
    print(f"Eligibility for discount: {evaluator1.is_eligible_for_discount()}")

    evaluator2 = DiscountEvaluator(False, 200)
    print(f"Eligibility for discount: {evaluator2.is_eligible_for_discount()}")