import sys
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == '__main__':
    n = 20
    result = fibonacci(n)
    print(*result)