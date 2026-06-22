class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Length 'b' cannot be zero for ratio calculation.")
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    length_a = 10
    length_b = 5
    print(calculator.get_ratio(length_a, length_b))