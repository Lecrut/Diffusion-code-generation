import statistics

class MeanCalculator:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid data type. Only numbers are allowed.")
        self.data.append(value)

    def calculate_mean(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        return statistics.mean(self.data)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_values = [10, 20, 30, 40, 50]
    for value in sample_values:
        calculator.add_data(value)
    try:
        mean_value = calculator.calculate_mean()
        print(f"The arithmetic mean is: {mean_value}")
    except ValueError as e:
        print(e)