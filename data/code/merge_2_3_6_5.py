def check_parity(value: int) -> bool:
    return (value & 1) != 0
if __name__ == '__main__':
    test_cases = [5, 6, 7]
    for num in test_cases:
        result = check_parity(num)
        print(f"Parity of {num}: {result}")