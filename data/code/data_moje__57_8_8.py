def generate_fibonacci(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n + 1):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == '__main__':
    fib_1000 = generate_fibonacci(1000)
    print(len(fib_1000))
    print(fib_1000[-1])