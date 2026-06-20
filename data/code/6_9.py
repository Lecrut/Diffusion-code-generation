class WeightCalculator:
    def __init__(self):
        self._unit = "kg"

    def calculate_difference(self, weight1, weight2):
        if weight1 < 0 or weight2 < 0:
            raise ValueError("Weights cannot be negative")
        return abs(weight1 - weight2)

    def get_unit(self):
        return self._unit

    def set_unit(self, new_unit):
        self._unit = new_unit

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight_a = 150.5
    weight_b = 120.0
    result = calculator.calculate_difference(weight_a, weight_b)
    print(result)
    current_unit = calculator.get_unit()
    print(current_unit)
    calculator.set_unit("lbs")
    print(calculator.get_unit())