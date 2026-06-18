def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    return (a and b > 0) and ((c >= 10.5) or not a)
if __name__ == '__main__':
    sample_a = True
    sample_b = -3
    sample_c = 20.7
    result = evaluate_nested_condition(sample_a, sample_b, sample_c)
    if result:
        print("Condition is true.")
    else:
        print("Condition is false.")