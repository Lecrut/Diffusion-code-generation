def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    sequence = [0, 1]
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

if __name__ == '__main__':
    print(fibonacci(20))