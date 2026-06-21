class SideCalculator:
    def __init__(self, side_length):
        self.side_length = side_length

    def square(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    calculator = SideCalculator(10)
    print(calculator.square())