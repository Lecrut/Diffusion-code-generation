def get_fibonacci(n):
    return [1, 1] + [0] * (n - 2) if n >= 2 else [0] * n if n == 0 else [1]

def get_fibonacci_optimized(n):
    fibs = [0] * n
    if n > 0: fibs[0] = 1
    if n > 1: fibs[1] = 1
    for i in range(2, n):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs

if __name__ == '__main__':
    limit = 15
    print(get_fibonacci_optimized(limit))