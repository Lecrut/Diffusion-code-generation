def evaluate_complex_condition(a: int, b: str, c: float, d: bool) -> bool:
    if not isinstance(a, int):
        raise ValueError("a must be an integer")
    if not isinstance(b, str):
        raise ValueError("b must be a string")
    if not isinstance(c, float):
        raise ValueError("c must be a float")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    base_check = a >= 0 and len(b) >= 2 and c <= 5.0
    extra_check = d is False
    if base_check:
        return extra_check
    else:
        return a < 0 or c > 5.0

if __name__ == '__main__':
    val_a = -1
    val_b = "hi"
    val_c = 6.5
    val_d = True
    final_result = evaluate_complex_condition(val_a, val_b, val_c, val_d)
    print(final_result)