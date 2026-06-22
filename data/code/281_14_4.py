class NumberSum:
    def __init__(self):
        self.numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = NumberSum()
    print(calculator.calculate_sum())