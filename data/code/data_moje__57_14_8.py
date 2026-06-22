def generate_fibonacci(n):
    fib = [1 if i < 2 else fib[-1] + fib[-2] for i in range(n)]
    return fib

if __name__ == '__main__':
    print(generate_fibonacci(15))