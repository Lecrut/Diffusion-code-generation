def is_even(n: int) -> bool:
    if n & 1:
        return False
    return True

if __name__ == '__main__':
    TEST_VALUES = [0, 1, 2, -2, 101, 1000]
    for val in TEST_VALUES:
        print(f"{val}: {is_even(val)}")