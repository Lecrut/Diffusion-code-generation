def get_area(side):
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == "__main__":
    TEST_VALUE = 10
    final_area = get_area(TEST_VALUE)
    print(final_area)