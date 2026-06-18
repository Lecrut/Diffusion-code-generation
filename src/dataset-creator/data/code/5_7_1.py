class Calculator:
    def __init__(self, initial_value):
        self._internal_value = initial_value
    def calculate_difference(self, external_value):
        return self._internal_value - external_value
if __name__ == '__main__':
    my_calc = Calculator(50)
    external_val1 = 20
    result1 = my_calc.calculate_difference(external_val1)
    print(f"Difference 1: {result1}")
    external_val2 = 75
    result2 = my_calc.calculate_difference(external_val2)
    print(f"Difference 2: {result2}")