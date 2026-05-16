class ValueChecker:
    def check_for_zero(self, number: int) -> bool:
        return number == 0
if __name__ == '__main__':
    checker = ValueChecker()
    sample1 = 0
    sample2 = 5
    sample3 = -10
    print(f"Checking {sample1}: {checker.check_for_zero(sample1)}")
    print(f"Checking {sample2}: {checker.check_for_zero(sample2)}")
    print(f"Checking {sample3}: {checker.check_for_zero(sample3)}")