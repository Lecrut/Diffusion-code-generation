class ZeroChecker:
    @staticmethod
    def is_zero(value):
        return value == 0

if __name__ == '__main__':
    checker = ZeroChecker()
    sample1 = 0
    sample2 = 5
    sample3 = -10
    print(f"Checking {sample1}: {checker.is_zero(sample1)}")
    print(f"Checking {sample2}: {checker.is_zero(sample2)}")
    print(f"Checking {sample3}: {checker.is_zero(sample3)}")