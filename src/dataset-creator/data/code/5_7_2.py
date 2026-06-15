class Calculator:
    def __init__(self, initial_value):
        self._internal_value = initial_value
    def calculate_difference(self, external_value):
        return self._internal_value - external_value
if __name__ == '__main__':
    calc = Calculator(100)
    external_val_1 = 45
    result_1 = calc.calculate_difference(external_val_1)
    print(f"Difference between internal value (100) and external value ({external_val_1}): {result_1}")
    calc2 = Calculator(250)
    external_val_2 = 300
    result_2 = calc2.calculate_difference(external_val_2)
    print(f"Difference between internal value (250) and external value ({external_val_2}): {result_2}")