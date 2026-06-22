from typing import List

def generate_fibonacci_terms(n: int) -> List[int]:
    if n <= 0:
        return []
    sequence: List[int] = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    current_index: int = 2
    while current_index < n:
        next_val: int = sequence[current_index - 1] + sequence[current_index - 2]
        sequence.append(next_val)
        current_index += 1
    return sequence

if __name__ == '__main__':
    target_term: int = 500
    result: List[int] = generate_fibonacci_terms(target_term)
    print(result[-1])