def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_sequence: list[int] = [0, 1]
    for i in range(2, n):
        next_value: int = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    return fib_sequence

if __name__ == '__main__':
    result: list[int] = generate_fibonacci(500)
    print(result)