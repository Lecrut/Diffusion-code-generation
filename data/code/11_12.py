class LengthCalculator:
    def get_ratio(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    calculator = LengthCalculator()
    length_a = 10
    length_b = 5
    ratio = calculator.get_ratio(length_a, length_b)
    print(ratio)