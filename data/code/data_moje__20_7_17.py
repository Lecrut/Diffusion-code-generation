EVEN_MASK = 1

def is_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & EVEN_MASK) == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, -4, -5]
    for val in test_values:
        print(is_even(val))