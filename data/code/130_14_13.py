class ZeroChecker:
    @staticmethod
    def is_zero(num):
        return num == 0

if __name__ == '__main__':
    x = -1
    result = ZeroChecker.is_zero(x)
    print(result)
    y = 0
    result = ZeroChecker.is_zero(y)
    print(result)