from typing import Tuple

def are_inputs_both_false(first: bool, second: bool) -> bool:
    is_first_false: bool = not first
    is_second_false: bool = not second
    both_conditions_hold: bool = is_first_false and is_second_false
    return both_conditions_hold

if __name__ == '__main__':
    sample_a: bool = True
    sample_b: bool = False
    outcome: bool = are_inputs_both_false(sample_a, sample_b)
    print(outcome)