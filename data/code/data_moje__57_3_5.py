from typing import List

def generate_fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence: List[int] = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

if __name__ == '__main__':
    target_term: int = 500
    result: List[int] = generate_fibonacci(target_term)
    print(result)