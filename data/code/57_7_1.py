def fibonacci_bitwise(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    a, b = (0, 1)
    for _ in range(2, n):
        a, b = (b, a + b)
        fibs.append(b)
    return fibs
if __name__ == '__main__':
    result = fibonacci_bitwise(100)
    print(result)