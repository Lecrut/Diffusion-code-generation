import operator
def evaluate_nested_condition(a: bool, b: int, c: float) -> bool:
    cond_1 = (a or not b) and ((c > 0.5) == True)
    is_positive_b = b >= 3
    final_result = cond_1 and (not is_positive_b or c < 1.0)
    return final_result
if __name__ == '__main__':
    sample_a: bool = True
    sample_b: int = 5
    sample_c: float = 2.7
    result = evaluate_nested_condition(sample_a, sample_b, sample_c)