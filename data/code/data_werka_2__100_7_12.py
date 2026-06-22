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
    is_non_empty_b = len(b) > 0
    is_short_c = c < 5.0
    is_true_d = d is True
    
    part_one = is_positive_a and is_non_empty_b
    part_two = is_short_c or is_true_d
    part_three = not (a == 0 and b == "")
    
    result = (part_one and part_two) or part_three
    return result

if __name__ == '__main__':
    sample_a = -5
    sample_b = "world"
    sample_c = 2.71
    sample_d = False
    
    final_outcome = evaluate_complex_condition(sample_a, sample_b, sample_c, sample_d)
    print(final_outcome)