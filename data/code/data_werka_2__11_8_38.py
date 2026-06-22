class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Length 'b' cannot be zero for division.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    length_a = 15
    length_b = 3
    ratio = calculator.get_ratio(length_a, length_b)
    print(ratio)