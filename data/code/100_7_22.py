def evaluate_complex_condition(a: int, b: str, c: float, d: bool) -> bool:
    if not isinstance(a, int):
        raise ValueError("a must be an integer")
    if not isinstance(b, str):
        raise ValueError("b must be a string")
    if not isinstance(c, float):
        raise ValueError("c must be a float")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    threshold = 50
    sum_val = a + int(c)
    is_valid_string = len(b) >= 2 and b.isalnum()
    logic_part_1 = sum_val > threshold
    logic_part_2 = d is True
    logic_part_3 = is_valid_string
    final_result = (logic_part_1 and logic_part_2) or logic_part_3
    return final_result

if __name__ == '__main__':
    val_a = 100
    val_b = "abc123"
    val_c = 25.5
    val_d = False
    outcome = evaluate_complex_condition(val_a, val_b, val_c, val_d)
    print(outcome)