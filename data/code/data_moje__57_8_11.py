def generate_fibonacci(n: int) -> list[int]:
    if n < 0:
        return []
    if n == 0:
        return [0]
    
    fib_sequence = [0, 1]
    for _ in range(2, n + 1):
        next_val = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_val)
    
    return fib_sequence

if __name__ == '__main__':
    result = generate_fibonacci(1000)
    print(result[1000])