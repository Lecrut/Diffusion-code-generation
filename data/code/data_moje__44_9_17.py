class NumberAverageCalculator:
    def __init__(self, numbers):
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list")
        if not all(isinstance(n, (int, float)) for n in numbers):
            raise ValueError("All elements must be numbers")
        if len(numbers) == 0:
            raise ValueError("List cannot be empty")
        self.numbers = numbers

    def get_average(self):
        total = 0
        count = 0
        for value in self.numbers:
            total += value
            count += 1
        return total / count

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    calculator = NumberAverageCalculator(sample_values)
    print(calculator.get_average())