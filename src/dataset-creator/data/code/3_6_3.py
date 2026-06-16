def check_parity(value: int) -> bool:
    return value & 1 != 0
if __name__ == '__main__':
    test_values = [5, -3, 0]
    for val in test_values:
        result = check_parity(val)
        print(f"Parity of {val}: {result}")