def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    a, b = 0, 1
    result = [a, b]
    for _ in range(2, n):
        a, b = b, a + b
        result.append(b)
    return result

if __name__ == '__main__':
    print(generate_fibonacci(100))