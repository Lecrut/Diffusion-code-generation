def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 3, -3]
    for value in sample_values:
        print(is_odd(value))