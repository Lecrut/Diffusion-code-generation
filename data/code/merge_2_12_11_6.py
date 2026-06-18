def is_even(number: int) -> bool:
    try:
        num = int(number)
        return bool(num % 2 == 0)
    except TypeError as te:
        raise TypeError(f"Input must be an integer or convertible float, got {type(number).__name__}.") from te
def is_odd(number: int) -> bool:
    try:
        num = int(number)
        return bool(num % 2 != 0)
    except TypeError as te:
        raise TypeError(f"Input must be an integer or convertible float, got {type(number).__name__}.") from te
if __name__ == '__main__':
    test_cases = [10, -3.5, "4", None]
    for case in test_cases:
        try:
            result_even = is_even(case)
            print(f"Number {case}: Even -> True")
        except (TypeError, ValueError):
            error_msg = f"{type(case).__name__ if isinstance(case, type(None)) else 'ValueError'} raised for input {case}"
            print(error_msg)
    try:
        result_odd = is_odd(7)
        assert result_odd == True
        print("Number 7: Odd -> True")
    except Exception as e:
        print(f"Unexpected error in main block: {e}")