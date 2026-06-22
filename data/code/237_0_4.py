def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    return sequence

if __name__ == '__main__':
    fib_sequence = fibonacci(10)
    print(fib_sequence)