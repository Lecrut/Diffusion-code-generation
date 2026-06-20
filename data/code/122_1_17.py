class AverageCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            raise ValueError("Input iterable cannot be empty")
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample1 = [1, 2, 3, 4, 5]
    sample2 = []
    sample3 = [10, 20, 30]

    try:
        avg1 = calculator.calculate_average(sample1)
        print(f"Average of {sample1}: {avg1}")
        avg3 = calculator.calculate_average(sample3)
        print(f"Average of {sample3}: {avg3}")
        calculator.calculate_average(sample2)
    except ValueError as e:
        print(f"Error: {e}")