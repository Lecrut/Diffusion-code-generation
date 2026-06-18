def check_parity(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return bool(number & 1)
if __name__ == '__main__':
    test_cases = [0, -5, 42, 99999]
    print("Parity Check Results:")
    for val in test_cases:
        is_odd = check_parity(val)
        status = "Odd" if is_odd else "Even"
        print(f"{val} -> {status}")