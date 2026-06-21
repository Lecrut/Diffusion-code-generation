import statistics

class MeanCalculator:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def calculate_mean(self):
        return statistics.mean(self.data)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = MeanCalculator(sample_values)
    print(f"The arithmetic mean is: {calculator.calculate_mean()}")