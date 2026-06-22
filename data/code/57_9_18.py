def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0] * n
    fibs[1] = 1
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
        fibs[i] = b
    return fibs

if __name__ == '__main__':
    print(generate_fibonacci(75))