def is_odd(n):
    return n & 1

if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 6]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")