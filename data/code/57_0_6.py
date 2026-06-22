def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
    
    return fib_sequence

if __name__ == '__main__':
    result = generate_fibonacci(100)
    print(result)