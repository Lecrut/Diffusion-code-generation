class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Denominator length 'b' cannot be zero.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    ratio = calculator.get_ratio(10, 5)
    print(ratio)