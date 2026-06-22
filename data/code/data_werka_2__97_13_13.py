from typing import List, Tuple

OPERANDS: List[bool] = [True, False]

def generate_and_truth_table() -> List[Tuple[bool, bool, bool]]:
    return [
        (a, b, a and b)
        for a in OPERANDS
        for b in OPERANDS
    ]

if __name__ == '__main__':
    table = generate_and_truth_table()
    for row in table:
        print(row)