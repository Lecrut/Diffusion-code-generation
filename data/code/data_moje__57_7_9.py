def calculate_fibonacci_bitwise(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        prev_prev = fib_sequence[i - 2]
        prev = fib_sequence[i - 1]
        next_val = prev_prev + prev
        fib_sequence.append(next_val)
    return fib_sequence

if __name__ == '__main__':
    result = calculate_fibonacci_bitwise(100)
    for i, val in enumerate(result):
        print(f"{i}: {val}")