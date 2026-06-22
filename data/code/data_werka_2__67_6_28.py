class SumCalculator:
    DEFAULT_VALUE1 = 0
    DEFAULT_VALUE2 = 0
    
    def __init__(self, value1=DEFAULT_VALUE1, value2=DEFAULT_VALUE2):
        self.value1 = value1
        self.value2 = value2
    
    @staticmethod
    def add_numbers(a, b):
        return a + b
    
    def calculate_sum(self):
        return SumCalculator.add_numbers(self.value1, self.value2)

if __name__ == '__main__':
    first_value = 4
    second_value = 9
    calculator_instance = SumCalculator(first_value, second_value)
    computed_sum = calculator_instance.calculate_sum()
    print(computed_sum)