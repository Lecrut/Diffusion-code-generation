class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0
    
    @staticmethod
    def _update(total, count, value):
        total += value
        count += 1
        return total, count
    
    def add_value(self, value):
        self.total, self.count = self._update(self.total, self.count, value)
        return self.total / self.count

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values = [1, 2, 3, 4, 5]
    print(calculator.add_value(sample_values[0]))
    print(calculator.add_value(sample_values[1]))
    print(calculator.add_value(sample_values[2]))
    print(calculator.add_value(sample_values[3]))
    print(calculator.add_value(sample_values[4]))