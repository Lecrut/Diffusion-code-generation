class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Length 'b' cannot be zero.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    ratio = calculator.get_ratio(10, 2)
    print(ratio)