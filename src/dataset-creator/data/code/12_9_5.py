def check_parity(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError("Input must be an integer.")
    if value < -10 or value > 10:
        raise ValueError(f"Value {value} is outside the allowed range of {-10} to {10}.")
    return bool(value % 2 == 0)
if __name__ == '__main__':
    test_cases = [-5, -3, 0, 4, 9]
    for case in test_cases:
        try:
            result = check_parity(case)
            print(f"Parity of {case}: {'Even' if result else 'Odd'}")
        except (TypeError, ValueError) as e:
            print(f"Error processing {case}: {e}")