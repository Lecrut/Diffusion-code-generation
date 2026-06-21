class ZeroChecker:
    TOLERANCE = 1e-10

    @staticmethod
    def is_zero(value):
        return abs(value) < ZeroChecker.TOLERANCE

if __name__ == '__main__':
    test_values = [
        0,
        1,
        -1,
        0.0001,
        -0.0001,
        0.0,
        -0.0,
        1e-308,
        1e-15,
        '0'
    ]
    for val in test_values:
        print(ZeroChecker.is_zero(val))