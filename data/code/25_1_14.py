class PriceCalculator:
    DISCOUNT_RATE = 0.15

    @staticmethod
    def compute_original_price(original_price: float) -> float:
        return original_price * (1 - PriceCalculator.DISCOUNT_RATE)

if __name__ == '__main__':
    calculator = PriceCalculator()
    sample_values = [100, 250]
    for value in sample_values:
        result = calculator.compute_original_price(value)
        print(result)