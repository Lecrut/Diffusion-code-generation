def generate_fibonacci(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    sequence = [0, 1]
    for _ in range(2, n):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    
    return sequence[:n]

if __name__ == '__main__':
    fib_sequence = generate_fibonacci(10)
    print(fib_sequence)