class AverageCalculator:
    def calculate_average(self, *args):
        if not args:
            return 0.0
        return sum(args) / len(args)

if __name__ == '__main__':
    calculator = AverageCalculator()
    print(calculator.calculate_average(10, 20, 30))
    print(calculator.calculate_average(5.5, 4.5, 6.5))