def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    sample_values = [42, -7, 0, 15, 1023]
    for value in sample_values:
        print(is_even(value))