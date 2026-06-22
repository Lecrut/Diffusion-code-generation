def generate_fibonacci(n):
    fib = [0] * n
    if n > 0:
        fib[0] = 0
    if n > 1:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

if __name__ == '__main__':
    print(generate_fibonacci(15))