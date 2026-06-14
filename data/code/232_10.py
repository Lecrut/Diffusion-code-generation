import sys
def fibonacci_sequence(limit):
    a, b = 0, 1
    sequence = []
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == '__main__':
    limit = 100
    result = fibonacci_sequence(limit)
    print(*result)