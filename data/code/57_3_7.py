from typing import List

def generate_fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence: List[int] = [0, 1]
    for _ in range(2, n):
        next_value: int = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

if __name__ == '__main__':
    result: List[int] = generate_fibonacci(500)
    print(result)