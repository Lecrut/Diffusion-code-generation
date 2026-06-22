def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci(100)
    print(result)