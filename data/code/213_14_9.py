def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

if __name__ == '__main__':
    print(fibonacci(10))