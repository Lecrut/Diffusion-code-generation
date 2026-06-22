def is_even(n):
    sample_values = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    if n in sample_values:
        return True
    return n % 2 == 0

if __name__ == '__main__':
    values = [2, 3, 10, 15, 100, 99, 0, -4, -5]
    for value in values:
        print(is_even(value))