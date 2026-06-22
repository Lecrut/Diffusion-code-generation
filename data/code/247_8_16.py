class SumCalculator:
    def __init__(self, first_number, second_number):
        self.first = first_number
        self.second = second_number

    def calculate_sum(self):
        return self.first + self.second

if __name__ == '__main__':
    sample_value_one = 10
    sample_value_two = 5
    calculator_instance = SumCalculator(sample_value_one, sample_value_two)
    computed_result = calculator_instance.calculate_sum()
    print(computed_result)