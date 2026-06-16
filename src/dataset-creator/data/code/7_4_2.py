from typing import Literal
def evaluate_condition(value: bool) -> bool:
    return value
if __name__ == '__main__':
    a = True
    b = False
    result_1 = (a and not b) or (not a and b)
    condition_a = evaluate_condition(result_1)
    condition_b = evaluate_condition(not condition_a)
    final_output: Literal[True, False] = condition_a if condition_b else condition_b
    print(final_output)