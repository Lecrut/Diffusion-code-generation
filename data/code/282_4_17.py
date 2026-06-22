class SequenceCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_list = [1, 5, 10, 2]
    result = calculator.calculate_sum(sample_list)
    print(f"The total of {sample_list} is: {result}")