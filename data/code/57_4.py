def fibonacci_first_n(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        fibs.append(b)
    return fibs

if __name__ == '__main__':
    print(fibonacci_first_n(200))