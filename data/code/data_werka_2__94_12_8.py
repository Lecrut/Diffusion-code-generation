from typing import Iterable

def has_any_truthy(items: Iterable) -> bool:
    return any(items)

EVALUATION_SET = {
    "zeros": [0, 0, 0],
    "mixed": [0, False, 1],
    "none_false": [None, False, 0],
    "all_true": [True, 1, "yes"],
    "empty": []
}

if __name__ == '__main__':
    for label, sequence in EVALUATION_SET.items():
        outcome = has_any_truthy(sequence)
        print(outcome)