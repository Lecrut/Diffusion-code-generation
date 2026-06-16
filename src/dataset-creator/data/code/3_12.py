from typing import Union
def is_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
def validate_number(value: object) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Input must be an integer or float.")
def check_parity_even(value: Union[int, float]) -> bool:
    validate_number(value)
    abs_val = abs(int(value)) % 2 == 0
    return abs_val
def check_parity_odd(value: Union[int, float]) -> bool:
    validate_number(value)
    result = not (abs(int(value)) % 2 == 0)
    return result
if __name__ == '__main__':
    test_cases_even = [4, -8.5, 17]
    print("Even parity checks:")
    for num in test_cases_even:
        try:
            res = check_parity_even(num)
            if isinstance(num, float):
                int_num = int(num)
                status = "N/A" if int_num % 2 != 0 else f"{int_num} is even"
            else:
                status = f"{num} {'is' if res else 'is not'} even"
        except TypeError as e:
            print(f"Error for {num}: {e}")
    test_cases_odd = [3, -2.5, 10]
    print("\nOdd parity checks:")
    for num in test_cases_odd:
        try:
            res = check_parity_odd(num)
            if isinstance(num, float):
                int_num = int(num)
                status = "N/A" if int_num % 2 != 0 else f"{int_num} is even"
            else:
                status = f"{num} {'is' if res else 'is not'} odd"
        except TypeError as e:
            print(f"Error for {num}: {e}")
    def smart_check(val):
        return val % 2 != 0 and abs(int(val)) > 10
    sample = -5.9
    result_smart = smart_check(sample) if isinstance(sample, (int, float)) else False
    print(f"\nCombined short-circuit check for {sample}: {'True' if result_smart else 'False'}")
    try:
        bad_input = "not a number"
        validate_number(bad_input)
    except TypeError as e:
        print(f"\nValidation caught error for invalid input '{bad_input}': {e}")