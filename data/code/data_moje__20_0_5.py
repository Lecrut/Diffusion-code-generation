def is_even(n):
    return n % 2 == 0

class EvenChecker:
    def check(self, n):
        return is_even(n)

if __name__ == '__main__':
    checker = EvenChecker()
    print(checker.check(4))
    print(checker.check(7))
    print(checker.check(0))
    print(checker.check(-3))
    print(checker.check(10))
    print(checker.check(-8))
    print(checker.check(15))
    print(checker.check(2))