class MeanCalculator:
    def calculate_mean(self, numbers):
        if not numbers:
            raise ValueError("Cannot calculate mean of an empty list")
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    print(calculator.calculate_mean([1, 2, 3, 4]))
    print(calculator.calculate_mean([-10, 20, -30]))
    try:
        print(calculator.calculate_mean([]))
    except ValueError as e:
        print(e)