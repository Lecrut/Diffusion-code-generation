from typing import List

def generate_fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_sequence: List[int] = [0, 1]
    index: int = 2
    while index < n:
        next_val: int = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
        index += 1
    return fib_sequence

if __name__ == '__main__':
    result: List[int] = generate_fibonacci(500)
    print(result[-1])