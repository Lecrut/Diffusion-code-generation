class NumberChecker:
    def is_negative(self, number):
        return number < 0

if __name__ == '__main__':
    checker = NumberChecker()
    print(f"Is -5 negative? {checker.is_negative(-5)}")
    print(f"Is 0 negative? {checker.is_negative(0)}")
    print(f"Is 10.5 negative? {checker.is_negative(10.5)}")
    print(f"Is -0.001 negative? {checker.is_negative(-0.001)}")