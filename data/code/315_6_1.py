import sys
def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence
if __name__ == '__main__':
    input_cycle_length = 10
    result = generate_fibonacci(input_cycle_length)
    print(*result)