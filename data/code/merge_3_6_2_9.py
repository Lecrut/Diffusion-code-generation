class WeightCalculator:
    @staticmethod
    def calculate_difference(weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights."""
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calc = WeightCalculator()

    # Hard-coded sample values
    w_a = 50.75
    w_b = 43.20

    diff = calc.calculate_difference(w_a, w_b)

    print(f"Difference between {w_a} and {w_b}: {diff}")