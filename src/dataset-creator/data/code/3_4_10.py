def check_parity(number: int) -> bool:
    return not (number & 1)
if __name__ == '__main__':
    test_cases = [42, -7, 0, 1]
    for val in test_cases:
        result = check_parity(val)
        print(f"Number {val}: Parity is {'even' if result else 'odd'}")