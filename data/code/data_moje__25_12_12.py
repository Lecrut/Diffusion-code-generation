class PriceCalculator:
    BASE_VALUE = 500.00
    DISCOUNT_RATE = 30.0

    @staticmethod
    def _compute_reduction(base, rate):
        return base * (rate / 100.0)

    @classmethod
    def get_discount_breakdown(cls):
        original = cls.BASE_VALUE
        percentage = cls.DISCOUNT_RATE
        reduction = cls._compute_reduction(original, percentage)
        final = original - reduction
        return {
            "original_price": original,
            "discount_percentage": percentage,
            "calculated_discount_value": reduction,
            "final_price": final
        }

if __name__ == '__main__':
    result = PriceCalculator.get_discount_breakdown()
    print(result)