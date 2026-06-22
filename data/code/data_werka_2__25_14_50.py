class ZeroChecker:
    SUPPORTED_TYPES = (int, float, complex)

    @staticmethod
    def is_zero(value):
        if isinstance(value, ZeroChecker.SUPPORTED_TYPES):
            return value == 0
        else:
            raise ValueError('Unsupported data type')

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(0.0))
    print(ZeroChecker.is_zero(0 + 0j))
    try:
        print(ZeroChecker.is_zero('0'))
    except ValueError as e:
        print(e)