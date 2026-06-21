def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

if __name__ == '__main__':
    n = 10
    result = fibonacci(n)
    print(result)