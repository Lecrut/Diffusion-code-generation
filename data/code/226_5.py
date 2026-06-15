import sys
def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
def print_sequence(sequence):
    for num in sequence:
        print(num, end=" ")
    print()
if __name__ == '__main__':
    n = 10
    full_sequence = generate_fibonacci(n)
    for _ in range(3):
        print_sequence(full_sequence)