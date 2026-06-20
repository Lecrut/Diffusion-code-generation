class ZeroChecker:
    @staticmethod
    def is_zero(num):
        return num == 0

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(42))
    print(ZeroChecker.is_zero(-1.5))
    print(ZeroChecker.is_zero(1e-09))