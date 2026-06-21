class FloatChecker:
    PI = 3.14

    @staticmethod
    def is_float_and_value(var):
        return isinstance(var, float) and var == FloatChecker.PI

if __name__ == '__main__':
    sample_values = [FloatChecker.PI, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in sample_values:
        print(FloatChecker.is_float_and_value(value))