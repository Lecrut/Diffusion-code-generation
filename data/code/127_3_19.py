class OddChecker:
    @staticmethod
    def is_odd(n):
        return (n & 1) == 1

if __name__ == '__main__':
    checker = OddChecker()
    print(checker.is_odd(5))
    print(checker.is_odd(4))
    print(checker.is_odd(0))
    print(checker.is_odd(-3))