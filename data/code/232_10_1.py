import sys
def print_fibonacci(limit):
    a, b = 0, 1
    sequence = []
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    print(*(sequence))
if __name__ == '__main__':
    limit = 100
    print_fibonacci(limit)