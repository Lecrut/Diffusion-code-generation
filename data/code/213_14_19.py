def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

if __name__ == '__main__':
    sample_n = 10
    output = fibonacci(sample_n)
    print(output)