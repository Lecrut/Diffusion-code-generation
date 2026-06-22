class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Length 'b' cannot be zero for division.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    ratio = calculator.get_ratio(10, 5)
    print(ratio)