def is_even(value: int) -> bool:
    if value is None:
        raise ValueError("Input cannot be None.")
    if isinstance(value, int):
        return value % 2 == 0
    if not isinstance(value, (int,)):
        raise TypeError(f"Expected an integer, got {type(value).__name__}.")
def check_parity(input_value: object) -> tuple[bool | None]:
    if isinstance(input_value, int):
        return input_value % 2 == 0
    raise TypeError(f"Input must be an integer, not {type(input_value).__name__}.")
if __name__ == '__main__':
    test_values = [10, -3.5, "five", None, True]
    for val in test_values:
        try:
            result = check_parity(val)
            print(f"Value {val}: Parity is {'even' if result else 'odd'}")
        except (TypeError, ValueError) as e:
            print(f"Error checking value {val}: {e}")