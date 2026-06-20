class EvenChecker:
    def is_even_and_positive(self, n):
        return n > 0 and not (n & 1)

if __name__ == '__main__':
    checker = EvenChecker()
    result1 = checker.is_even_and_positive(4)
    print(f"Is 4 even and positive? {result1}")
    result2 = checker.is_even_and_positive(-2)
    print(f"Is -2 even and positive? {result2}")
    result3 = checker.is_even_and_positive(0)
    print(f"Is 0 even and positive? {result3}")
    result4 = checker.is_even_and_positive(3)
    print(f"Is 3 even and positive? {result4}")