from typing import List

def generate_fibonacci_terms(count: int) -> List[int]:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    sequence: List[int] = [0, 1]
    for _ in range(2, count):
        next_val: int = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == '__main__':
    target_index: int = 500
    result: List[int] = generate_fibonacci_terms(target_index)
    print(len(result))
    print(result[-1])