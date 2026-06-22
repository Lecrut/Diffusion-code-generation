def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, n):
        c = a + b
        sequence.append(c)
        a = b
        b = c
    return sequence

if __name__ == '__main__':
    result = fibonacci_sequence(100)
    print(result)