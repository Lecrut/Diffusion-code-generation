def print_fibonacci_sequence(n):
    if n <= 0:
        return
    if n == 1:
        print(1)
        print(1)
        return
    a, b = 1, 1
    for _ in range(n - 2):
        next_val = a + b
        print(next_val)
        a = b
        b = next_val
if __name__ == '__main__':
    print_fibonacci_sequence(10)