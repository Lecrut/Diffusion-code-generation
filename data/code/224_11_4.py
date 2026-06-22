class AverageCalculator:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def calculate_average(self):
        total = sum(self.sequence)
        count = len(self.sequence)
        return total / count

if __name__ == '__main__':
    calculator = AverageCalculator([100, 200, 300])
    average = calculator.calculate_average()
    print(average)