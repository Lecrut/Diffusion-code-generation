import sys
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    return sequence
if __name__ == '__main__':
    n = 20
    fib_sequence = generate_fibonacci(n)
    print(*fib_sequence)