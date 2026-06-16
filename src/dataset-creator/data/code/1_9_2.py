from typing import Any
def evaluate_nested_condition(
    a: bool, b: bool, c: int, d: float
) -> bool:
    condition_1 = (a and not b) or (c > 5)
    condition_2 = ((d >= 0.0) if a else False) and (b == True)
    return condition_1 and condition_2
if __name__ == '__main__':
    sample_a: bool = True
    sample_b: bool = False
    sample_c: int = 6
    sample_d: float = -0.5
    result = evaluate_nested_condition(sample_a, sample_b, sample_c, sample_d)
    if result:
        print("The nested condition is TRUE.")
    else:
        print("The nested condition is FALSE.")