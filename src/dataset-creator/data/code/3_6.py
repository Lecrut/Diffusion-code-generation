def check_parity(value: int) -> bool:
    return (value & 1) != 0
if __name__ == '__main__':
    test_cases = [0b0, 0b1, 0x3FF]
    for num in test_cases:
        print(f"Parity of {num}: {check_parity(num)}")