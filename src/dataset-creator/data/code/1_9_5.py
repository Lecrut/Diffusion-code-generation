import operator
def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    return (a and ((b > 10) or (c < -5.0)) and not (operator.add(b, c) > 20))
if __name__ == '__main__':
    result = evaluate_nested_condition(True, 15, -3.5)
    print(result)