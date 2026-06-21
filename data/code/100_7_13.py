def evaluate_complex_condition(a: int, b: int, c: str, d: bool) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")
    if not isinstance(c, str):
        raise ValueError("c must be a string")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    condition_1 = a > 0 and b < 10
    condition_2 = c.startswith("x") or c.endswith("y")
    condition_3 = d is True
    
    result = (condition_1 and condition_2) or (condition_3 and not condition_1)
    return result

if __name__ == '__main__':
    a_val = 5
    b_val = 3
    c_val = "xy"
    d_val = False
    
    outcome = evaluate_complex_condition(a_val, b_val, c_val, d_val)
    print(outcome)