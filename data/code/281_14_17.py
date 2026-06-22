class NumberSum:
    NUMBERS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    @staticmethod
    def calculate_sum():
        return sum(NumberSum.NUMBERS)

if __name__ == '__main__':
    calculator = NumberSum()
    print(calculator.calculate_sum())