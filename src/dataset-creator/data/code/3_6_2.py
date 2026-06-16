def check_parity(value: int) -> bool:
    return (value & 1) != 0
if __name__ == '__main__':
    test_cases = [0b1010, 0b1111, -5]
    for case in test_cases:
        result = check_parity(case)
        print(f"Parity of {case}: {result}")