class NumberChecker:
    @staticmethod
    def is_zero(number):
        return number == 0

if __name__ == '__main__':
    checker = NumberChecker()
    print(f"Is 0 zero? {checker.is_zero(0)}")
    print(f"Is 0.0 zero? {checker.is_zero(0.0)}")
    print(f"Is 1 zero? {checker.is_zero(1)}")
    print(f"Is -1 zero? {checker.is_zero(-1)}")
    print(f"Is 3.14 zero? {checker.is_zero(3.14)}")