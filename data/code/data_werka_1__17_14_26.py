def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, -4, -5]
    for value in sample_values:
        print(is_even(value))