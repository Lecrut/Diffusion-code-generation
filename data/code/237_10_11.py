def generate_fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == '__main__':
    fib_sequence = generate_fibonacci(20)
    print(fib_sequence)