class FloatChecker:
    def __init__(self, value):
        self.value = value

    def is_float_and_pi(self):
        return isinstance(self.value, float) and self.value == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in sample_values:
        checker = FloatChecker(value)
        print(checker.is_float_and_pi())