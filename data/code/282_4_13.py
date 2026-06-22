class SequenceCalculator:
    def calculate_sum(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total

    @staticmethod
    def format_result(numbers, total):
        return f"The sum of {numbers} is: {total}"

if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_list = [1, 5, 10, 2]
    result = calculator.calculate_sum(sample_list)
    print(calculator.format_result(sample_list, result))