class Calculator:
    def __init__(self, initial_value):
        self._internal_value = initial_value
    def calculate_difference(self, external_value):
        return self._internal_value - external_value
if __name__ == '__main__':
    my_calc = Calculator(100)
    external_val_1 = 30
    result_1 = my_calc.calculate_difference(external_val_1)
    print(f"Difference between internal value (100) and external value ({external_val_1}): {result_1}")
    my_calc_2 = Calculator(50)
    external_val_2 = 75
    result_2 = my_calc_2.calculate_difference(external_val_2)
    print(f"Difference between internal value (50) and external value ({external_val_2}): {result_2}")