class NumberChecker:
    def is_even_and_positive(self, n):
        return n > 0 and not (n & 1)

if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.is_even_and_positive(4))
    print(checker.is_even_and_positive(-2))
    print(checker.is_even_and_positive(0))
    print(checker.is_even_and_positive(3))