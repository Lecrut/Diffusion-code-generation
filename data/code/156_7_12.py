class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    test_list_1 = [1, 2, 3, 4, 5]
    test_list_2 = [10, 20, 30]
    test_list_3 = []
    try:
        avg1 = calculator.calculate_average(test_list_1)
        print(f"Average of {test_list_1}: {avg1}")
        avg2 = calculator.calculate_average(test_list_2)
        print(f"Average of {test_list_2}: {avg2}")
        calculator.calculate_average(test_list_3)
    except ValueError as e:
        print(f"Error: {e}")