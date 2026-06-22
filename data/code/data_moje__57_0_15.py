def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    a, b = 0, 1
    sequence = [0, 1]
    
    for _ in range(2, n):
        next_val = a + b
        sequence.append(next_val)
        a = b
        b = next_val
    
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci(100)
    print(result)