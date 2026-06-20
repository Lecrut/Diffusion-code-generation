class ZeroChecker:
    @staticmethod
    def is_zero(value):
        try:
            return value == 0
        except TypeError:
            return False

if __name__ == '__main__':
    values = [1, 0, -3, "zero", None, True]
    for val in values:
        print(f"The value {val} is zero: {ZeroChecker.is_zero(val)}")