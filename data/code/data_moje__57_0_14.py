def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    a, b = 0, 1
    sequence = [a, b]
    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)
    return sequence

if __name__ == '__main__':
    print(generate_fibonacci(100))