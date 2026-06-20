class ZeroChecker:
    @staticmethod
    def is_zero(number):
        return number == 0

if __name__ == '__main__':
    print(ZeroChecker.is_zero(0))
    print(ZeroChecker.is_zero(1))