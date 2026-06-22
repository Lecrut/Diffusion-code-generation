class MovingAverage:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_value(self, value):
        self.total += value
        self.count += 1
        return self.total / self.count

if __name__ == '__main__':
    calculator = MovingAverage()
    sample_values = [1, 2, 3, 4, 5]
    print(calculator.add_value(sample_values[0]))
    print(calculator.add_value(sample_values[1]))
    print(calculator.add_value(sample_values[2]))
    print(calculator.add_value(sample_values[3]))
    print(calculator.add_value(sample_values[4]))