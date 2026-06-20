class ZeroChecker:
    def is_zero(self, number):
        return number == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    print(f"is_zero(0): {checker.is_zero(0)}")
    print(f"is_zero(5): {checker.is_zero(5)}")
    print(f"is_zero(-0): {checker.is_zero(-0)}")
    print(f"is_zero(3.14): {checker.is_zero(3.14)}")