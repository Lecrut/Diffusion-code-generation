class OddNumberChecker:
    @staticmethod
    def is_odd(n):
        return n & 1 == 1

if __name__ == '__main__':
    checker = OddNumberChecker()
    print(checker.is_odd(3))
    print(checker.is_odd(4))