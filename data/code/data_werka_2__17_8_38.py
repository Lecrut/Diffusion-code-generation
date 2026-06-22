def is_even(n):
    return n & 1 == 0

if __name__ == '__main__':
    sample_values = [10, -5, 3, 8, 7]
    for value in sample_values:
        print(is_even(value))