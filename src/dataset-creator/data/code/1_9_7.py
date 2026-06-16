def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    return (a and b > 0) and ((c < 10.5) or not a)
if __name__ == '__main__':
    result = evaluate_nested_condition(True, -5, 3.2)
    print(result)