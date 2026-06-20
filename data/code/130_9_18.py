class ZeroDetector:

    @staticmethod
    def is_zero(value):
        try:
            return value == 0
        except TypeError:
            return False
if __name__ == '__main__':
    print(ZeroDetector.is_zero(0))
    print(ZeroDetector.is_zero(1))
    print(ZeroDetector.is_zero('0'))
    print(ZeroDetector.is_zero(None))
    print(ZeroDetector.is_zero([0]))