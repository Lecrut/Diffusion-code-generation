def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, -1, -2, 0]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")