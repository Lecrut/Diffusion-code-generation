def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")