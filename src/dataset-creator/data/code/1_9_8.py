import operator
def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    return (a and ((b > 10) or not c)) and (((c * 2) >= 5.0) == True)
if __name__ == '__main__':
    sample_a = True
    sample_b = 15
    sample_c = 3.7
    result = evaluate_nested_condition(sample_a, sample_b, sample_c)
    if result:
        print("Condition is TRUE")
    else:
        print("Condition is FALSE")