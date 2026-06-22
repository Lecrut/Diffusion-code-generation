class AverageCalculator:

    @staticmethod
    def validate_input(numbers):
        return all((isinstance(num, (int, float)) for num in numbers))

    @staticmethod
    def calculate_average(numbers):
        if not AverageCalculator.validate_input(numbers):
            return None
        total = sum(numbers)
        count = len(numbers)
        return total / count
if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [10, 20, 30, 40, 50]
    average_result = calculator.calculate_average(sample_numbers)
    if average_result is not None:
        print(f'The average of the entered numbers is: {average_result}')
    else:
        print('Invalid input detected. Please enter only numbers.')