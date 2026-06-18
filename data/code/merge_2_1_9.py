import operator
def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    return (a and (b > 10 or c < -5.0)) or ((not a) and (c >= 0))
if __name__ == '__main__':
    sample_a = True
    sample_b = 20
    sample_c = -3.5
    result = evaluate_nested_condition(sample_a, sample_b, sample_c)
    if not isinstance(result, bool):
        raise TypeError("The function must return a boolean value.")
    print(f"Result: {result}")