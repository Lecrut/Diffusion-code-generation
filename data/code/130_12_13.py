def is_zero(value: int) -> bool:
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value == 0

if __name__ == '__main__':
    sample1 = 0
    sample2 = 5
    sample3 = -10
    print(f"Checking {sample1}: {is_zero(sample1)}")
    print(f"Checking {sample2}: {is_zero(sample2)}")
    print(f"Checking {sample3}: {is_zero(sample3)}")