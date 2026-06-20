def is_odd(n):
    return n & 1

if __name__ == '__main__':
    sample_values = [3, 4, 5, 6, 7]
    for value in sample_values:
        print(is_odd(value))