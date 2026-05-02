class ValueChecker:
    def check_for_zero(self, value: int) -> bool:
        return value == 0
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"Checking 0: {checker.check_for_zero(0)}")
    print(f"Checking 5: {checker.check_for_zero(5)}")
    print(f"Checking -3: {checker.check_for_zero(-3)}")
    print(f"Checking 0.0 (if input is float, though type hint expects int): {checker.check_for_zero(0.0)}")