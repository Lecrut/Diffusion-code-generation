class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Length 'b' cannot be zero.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    try:
        ratio = calculator.get_ratio(15, 3)
        print(ratio)
    except ValueError as e:
        print(e)