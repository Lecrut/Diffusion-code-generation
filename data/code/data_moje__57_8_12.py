def fibonacci_sequence(n):
    if n < 0:
        raise ValueError("Index must be non-negative")
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n + 1):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == '__main__':
    result = fibonacci_sequence(1000)
    print(result[-1])