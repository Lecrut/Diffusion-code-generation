from typing import List

def generate_fibonacci_up_to_n(n: int) -> List[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence: List[int] = [0, 1]
    for i in range(2, n):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
    
    return sequence

if __name__ == '__main__':
    limit = 500
    result = generate_fibonacci_up_to_n(limit)
    print(f"First {limit} Fibonacci numbers:")
    print(result)
    print(f"The 500th Fibonacci number is: {result[-1]}")