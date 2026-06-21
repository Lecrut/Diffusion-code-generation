def evaluate_complex_condition(a: int, b: int, c: str, d: bool) -> bool:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")
    if not isinstance(c, str):
        raise ValueError("c must be a string")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    condition_1 = a > 0 and b < 100
    condition_2 = len(c) > 3
    condition_3 = d is True
    
    if condition_1:
        if condition_2:
            return condition_3
        else:
            return False
    else:
        return not condition_3

if __name__ == '__main__':
    result = evaluate_complex_condition(10, 50, "hello", True)
    print(result)