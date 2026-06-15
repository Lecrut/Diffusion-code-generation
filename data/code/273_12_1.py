import sys
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_fib = sequence[-1] + sequence[-2]
            sequence.append(next_fib)
        return sequence
if __name__ == '__main__':
    limit = 15
    fib_sequence = generate_fibonacci(limit)
    print(*fib_sequence)