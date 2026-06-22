def is_positive(n):
    return n > 0

if __name__ == '__main__':
    sample_values = [0, -1, 5, -10, 23]
    for value in sample_values:
        print(is_positive(value))