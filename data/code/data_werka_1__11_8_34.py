class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Length 'b' cannot be zero for ratio calculation.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    try:
        result = calculator.get_ratio(10, 2)
        print(result)
    except ValueError as e:
        print(e)