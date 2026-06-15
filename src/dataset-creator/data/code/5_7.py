class Calculator:
    def __init__(self, initial_value):
        self._internal_value = initial_value
    def calculate_difference(self, external_value):
        return self._internal_value - external_value
if __name__ == '__main__':
    calc = Calculator(100)
    external_a = 45
    result_a = calc.calculate_difference(external_a)
    print(f"Difference between internal value (100) and external value ({external_a}): {result_a}")
    calc2 = Calculator(250)
    external_b = 300
    result_b = calc2.calculate_difference(external_b)
    print(f"Difference between internal value (250) and external value ({external_b}): {result_b}")