def evaluate_complex_condition(a: int, b: int, c: str, d: bool) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")
    if not isinstance(c, str):
        raise ValueError("c must be a string")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    condition_one = a > 0 and b < 100
    condition_two = len(c) > 3 and c.isalpha()
    condition_three = d is True
    
    result = (condition_one and condition_two) or (condition_three and not condition_one)
    return result

if __name__ == '__main__':
    a_val = 10
    b_val = 50
    c_val = "hello"
    d_val = False
    
    outcome = evaluate_complex_condition(a_val, b_val, c_val, d_val)
    print(outcome)