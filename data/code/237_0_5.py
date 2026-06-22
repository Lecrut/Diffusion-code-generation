def generate_fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    sequence = [0, 1]
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    
    return sequence[:n]

if __name__ == '__main__':
    try:
        fib_sequence = generate_fibonacci(10)
        print(fib_sequence)
    except ValueError as e:
        print(e)