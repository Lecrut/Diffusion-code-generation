def fibonacci(n):
    fib_cache = {0: 0, 1: 1}
    for i in range(2, n):
        fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]
    return [fib_cache[i] for i in range(n)]

if __name__ == '__main__':
    print(fibonacci(20))