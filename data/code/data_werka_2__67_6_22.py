class SumCalculator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def sum_of_attributes(self):
        return self.value1 + self.value2
if __name__ == '__main__':
    first_value = 8
    second_value = 15
    calculator_instance = SumCalculator(first_value, second_value)
    computed_sum = calculator_instance.sum_of_attributes()
    print(computed_sum)