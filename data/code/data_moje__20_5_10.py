def is_even(n):
    return True if n % 2 == 0 else False

if __name__ == '__main__':
    sample_values = [15, 22, 0, -4, 99, -1]
    for val in sample_values:
        print(is_even(val))