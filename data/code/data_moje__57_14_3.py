def generate_fibonacci(n):
    fib = [0, 1]
    return [fib.append(fib[-1] + fib[-2]) or fib[-1] for _ in range(2, n)]

if __name__ == '__main__':
    print(generate_fibonacci(15))