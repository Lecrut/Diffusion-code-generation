def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    return fib_sequence

if __name__ == '__main__':
    count = 20
    result = generate_fibonacci(count)
    print(result)