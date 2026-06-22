class ZeroChecker:
    TOLERANCE = 1e-308

    @staticmethod
    def is_zero(value):
        return abs(value) < ZeroChecker.TOLERANCE

if __name__ == '__main__':
    test_values = [
        0,
        -0.0,
        1,
        -1,
        0.001,
        -0.001,
        1e-308,
        -1e-308
    ]
    
    for val in test_values:
        print(f"{val}: {ZeroChecker.is_zero(val)}")