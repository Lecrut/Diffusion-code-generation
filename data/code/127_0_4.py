class NumberChecker:
    def is_odd(self, n):
        return n & 1

if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.is_odd(3))
    print(checker.is_odd(4))