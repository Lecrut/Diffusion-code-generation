def bitwise_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_val = (fib_sequence[i-1] << 1) - fib_sequence[i-2]
        fib_sequence.append(next_val)
    return fib_sequence

if __name__ == '__main__':
    terms = 100
    result = bitwise_fibonacci(terms)
    for val in result:
        print(val)