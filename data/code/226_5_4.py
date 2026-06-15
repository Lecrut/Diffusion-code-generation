import sys
def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == '__main__':
    base_length = 10
    full_sequence = []
    for _ in range(3):
        fib_part = generate_fibonacci(base_length)
        full_sequence.extend(fib_part)
    print(" ".join(map(str, full_sequence)))