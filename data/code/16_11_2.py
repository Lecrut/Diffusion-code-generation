class NumberChecker:
    def check_positivity(self, value):
        return value > 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(f"Is 5 positive? {checker.check_positivity(5)}")
    print(f"Is -3 positive? {checker.check_positivity(-3)}")
    print(f"Is 0 positive? {checker.check_positivity(0)}")
    print(f"Is 100 positive? {checker.check_positivity(100)}")
    print(f"Is -0.001 positive? {checker.check_positivity(-0.001)}")