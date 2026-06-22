def evaluate_logical_state(x: int, y: float, z: str, w: bool) -> bool:
    if not isinstance(x, int):
        raise ValueError("x must be an integer")
    if not isinstance(y, float):
        raise ValueError("y must be a float")
    if not isinstance(z, str):
        raise ValueError("z must be a string")
    if not isinstance(w, bool):
        raise ValueError("w must be a boolean")
    
    base_positive = x > 0
    length_check = len(z) > 2
    threshold_check = y < 5.0
    
    group_a = base_positive and length_check
    group_b = threshold_check or w
    
    intermediate = group_a and group_b
    final_override = not base_positive and w
    
    return intermediate or final_override

if __name__ == '__main__':
    result = evaluate_logical_state(10, 3.5, "abc", True)
    print(result)