import math

class ZeroChecker:

    def __init__(self, tolerance=1e-10):
        self.tolerance = tolerance

    def is_zero(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return abs(value) < self.tolerance
        elif isinstance(value, complex):
            return abs(value.real) < self.tolerance and abs(value.imag) < self.tolerance
        else:
            raise ValueError(f'Unsupported type: {type(value)}')

    def check_values(self, values):
        return [self.is_zero(value) for value in values]
if __name__ == '__main__':
    sample_values = [0, 1e-10, -1e-10, 0.0, 1 + 0j, 0 + 0j, 1e-15 + 1e-15j]
    zero_checker = ZeroChecker()
    result = zero_checker.check_values(sample_values)
    print(result)
    single_value_result = zero_checker.is_zero(1e-10)
    print(single_value_result)
    complex_value_result = zero_checker.is_zero(1e-15 + 1e-15j)
    print(complex_value_result)