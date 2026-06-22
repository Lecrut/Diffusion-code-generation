def evaluate_complex_condition(a: int, b: str, c: float, d: bool) -> bool:
    if not isinstance(a, int):
        raise ValueError("a must be an integer")
    if not isinstance(b, str):
        raise ValueError("b must be a string")
    if not isinstance(c, float):
        raise ValueError("c must be a float")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    condition_1 = a > 0 and len(b) > 0
    condition_2 = c < 10.0 or d is True
    condition_3 = not (a == 0 and b == "")
    
    result = (condition_1 and condition_2) or condition_3
    
    return result

if __name__ == '__main__':
    sample_a = 5
    sample_b = "hello"
    sample_c = 3.14
    sample_d = False
    
    outcome = evaluate_complex_condition(sample_a, sample_b, sample_c, sample_d)
    print(outcome)