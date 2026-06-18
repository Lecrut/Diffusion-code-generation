def check_parity(number: int) -> bool:
    return bool(number & 1)
if __name__ == '__main__':
    test_cases = [0, -5, 42, -3, 99]
    print("Parity Check Results:")
    for val in test_cases:
        is_even = check_parity(val)
        status = "Even" if is_even else "Odd"
        print(f"{val}: {status}")