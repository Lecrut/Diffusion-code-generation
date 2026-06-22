class ZeroChecker:
    def is_zero(self, value):
        if isinstance(value, (int, float)):
            return value == 0
        elif isinstance(value, complex):
            return value == 0 + 0j
        else:
            raise ValueError('Unsupported data type')

if __name__ == '__main__':
    checker = ZeroChecker()
    print(checker.is_zero(0))
    print(checker.is_zero(0.0))
    print(checker.is_zero(0 + 0j))
    try:
        print(checker.is_zero('0'))
    except ValueError as e:
        print(e)