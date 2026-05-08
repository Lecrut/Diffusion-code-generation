class ValueChecker:
    def check_for_zero(self, number: int) -> bool:
        return number == 0
if __name__ == '__main__':
    checker = ValueChecker()
    value1 = 0
    value2 = 5
    value3 = -10
    result1 = checker.check_for_zero(value1)
    result2 = checker.check_for_zero(value2)
    result3 = checker.check_for_zero(value3)
    print(f"Checking {value1}: {result1}")
    print(f"Checking {value2}: {result2}")
    print(f"Checking {value3}: {result3}")