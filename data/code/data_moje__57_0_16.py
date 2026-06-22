def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    a, b = 0, 1
    
    for _ in range(2, n):
        a, b = b, a + b
        fib_sequence.append(b)
    
    return fib_sequence

if __name__ == '__main__':
    result = generate_fibonacci(100)
    print(result)