def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence

if __name__ == '__main__':
    result = generate_fibonacci(1000)
    print(result[1000])