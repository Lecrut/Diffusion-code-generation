class NumberChecker:
    @staticmethod
    def is_zero(value):
        return value == 0

if __name__ == '__main__':
    checker = NumberChecker()
    print(f"Is 0 zero? {checker.is_zero(0)}")
    print(f"Is 5 zero? {checker.is_zero(5)}")
    print(f"Is -10.0 zero? {checker.is_zero(-10.0)}")