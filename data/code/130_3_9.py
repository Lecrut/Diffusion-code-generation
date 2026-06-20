class ZeroChecker:
    def is_zero(self, value):
        return value == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    print(f"Checking 0: {checker.is_zero(0)}")
    print(f"Checking 5: {checker.is_zero(5)}")
    print(f"Checking -3: {checker.is_zero(-3)}")
    print(f"Checking 0.0: {checker.is_zero(0.0)}")