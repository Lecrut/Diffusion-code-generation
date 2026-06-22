def fibonacci_up_to_term(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence: list[int] = [0, 1]
    for i in range(2, n):
        next_val = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_val)
    return sequence

if __name__ == '__main__':
    result = fibonacci_up_to_term(500)
    print(result)