from typing import List

def generate_fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence: List[int] = [0, 1]
    for _ in range(2, n):
        next_val: int = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == "__main__":
    limit: int = 500
    result: List[int] = generate_fibonacci(limit)
    print(result)