class OddChecker:
    @staticmethod
    def check_odd(n):
        return (n & 1) == 1

if __name__ == '__main__':
    print(OddChecker.check_odd(5))
    print(OddChecker.check_odd(4))
    print(OddChecker.check_odd(0))
    print(OddChecker.check_odd(-3))