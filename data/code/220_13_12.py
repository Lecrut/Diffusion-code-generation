if __name__ == '__main__':
    numbers = [50, 60, 70]
    avg_calculator = AverageCalculator(numbers)
    print(avg_calculator.calculate_average())

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)