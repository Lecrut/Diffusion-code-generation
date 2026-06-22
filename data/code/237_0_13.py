def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    
    return sequence

if __name__ == '__main__':
    n = 10
    fib_sequence = fibonacci_sequence(n)
    print(fib_sequence)