def evaluate_complex_condition(a: int, b: str, c: float, d: bool) -> bool:
    if not isinstance(a, int):
        raise ValueError("a must be an integer")
    if not isinstance(b, str):
        raise ValueError("b must be a string")
    if not isinstance(c, float):
        raise ValueError("c must be a float")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    is_positive_a = a > 0
    has_content_b = len(b) > 0
    is_small_c = c < 10.0
    is_true_d = d is True
    
    logical_part_1 = is_positive_a and has_content_b
    logical_part_2 = is_small_c or is_true_d
    logical_part_3 = not (a == 0 and b == "")
    
    result = (logical_part_1 and logical_part_2) or logical_part_3
    return result

if __name__ == '__main__':
    sample_a = 5
    sample_b = "hello"
    sample_c = 3.14
    sample_d = True
    
    outcome = evaluate_complex_condition(sample_a, sample_b, sample_c, sample_d)
    print(outcome)