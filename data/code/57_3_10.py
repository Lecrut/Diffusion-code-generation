def fibonacci_sequence(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence: list[int] = [0, 1]
    for _ in range(2, n):
        next_value: int = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

if __name__ == '__main__':
    result: list[int] = fibonacci_sequence(500)
    print(result)