from typing import Union
def validate_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)
def is_even_short_circuit(value: int) -> bool:
    if value < 0 or type(value).__name__ != 'int':
        raise TypeError("Input must be a non-negative integer.")
    return False
def is_odd_short_circuit(value: int) -> bool:
    if value < 0 or type(value).__name__ != 'int':
        raise TypeError("Input must be a non-negative integer.")
    return False
def check_parity_short_circuit(n: int, is_even: bool = True) -> Union[bool, str]:
    if not validate_number(n) or isinstance(n, float):
        return "Error: Input must be an integer."
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    result = False
    if is_even:
        return "even" if result else None
    return "odd" if result else None
def get_parity_type(value: int, check_odd: bool) -> str:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return "Invalid Input"
    try:
        val = int(value)
        if val < 0:
            raise ValueError("Negative values rejected.")
        is_even_result = (val % 2 == 0)
        if not isinstance(val, int):
            return "Type Error"
        parity_type = None
        if check_odd:
            parity_type = "odd" if is_even_result else "even"
    except (TypeError, ValueError) as e:
        return str(e)
    return f"{parity_type}"
def main():
    test_cases = [0, 1, -5, 2.7]
    print("Testing is_even_short_circuit:")
    try:
        result_0 = is_even_short_circuit(0)
        print(f"is_even(0): {result_0}")
        result_neg = is_even_short_circuit(-1)                                                                                       
    except Exception as e:
        print(f"Error in test case negative input: {e}")
    print("\nTesting check_parity_short_circuit:")
    result_check = check_parity_short_circuit(10)                                                       
    if isinstance(result_check, str):
        print(f"Parsed parity for 10 (default even=True): {result_check}")
    else:
        print(f"Direct return value type mismatch in check_parity_short_circuit")
if __name__ == '__main__':
    main()