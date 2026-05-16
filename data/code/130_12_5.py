class ValueChecker:
    def check_for_zero(self, number: int) -> bool:
        return number == 0
if __name__ == '__main__':
    checker = ValueChecker()
    sample1 = 0
    sample2 = 5
    sample3 = -10
    result1 = checker.check_for_zero(sample1)
    result2 = checker.check_for_zero(sample2)
    result3 = checker.check_for_zero(sample3)
    print(f"Checking {sample1}: {result1}")
    print(f"Checking {sample2}: {result2}")
    print(f"Checking {sample3}: {result3}")