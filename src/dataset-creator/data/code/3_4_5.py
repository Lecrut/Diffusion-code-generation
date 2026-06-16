def check_parity(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be a non-boolean integer.")
    return n % 2 == 0
if __name__ == '__main__':
    test_cases = [1, -4, 0, 17]
    for val in test_cases:
        result = check_parity(val)
        print(f"Parity of {val}: {'Even' if result else 'Odd'}")