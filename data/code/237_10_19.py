def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence[:n]

if __name__ == '__main__':
    try:
        print(fibonacci(20))
    except ValueError as e:
        print(e)