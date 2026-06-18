import operator
def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    return (a and ((b > 10) or (c < -5.0)) and not (operator.add(b, c) > 20))
if __name__ == '__main__':
    sample_a = True
    sample_b = 8
    sample_c = -3.5
    result = evaluate_nested_condition(sample_a, sample_b, sample_c)
    print(result)