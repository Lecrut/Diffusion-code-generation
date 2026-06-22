def generate_fibonacci_terms(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci_terms(100)
    print(result)