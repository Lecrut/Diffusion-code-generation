ZERO = 0

def is_zero(value: int) -> bool:
    return value == ZERO

if __name__ == '__main__':
    sample1 = 0
    sample2 = 5
    sample3 = -10
    print(f"Checking {sample1}: {is_zero(sample1)}")
    print(f"Checking {sample2}: {is_zero(sample2)}")
    print(f"Checking {sample3}: {is_zero(sample3)}")