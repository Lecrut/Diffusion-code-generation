def is_odd(n):
    parity_map = {0: False, 1: True}
    return parity_map[n % 2]

if __name__ == '__main__':
    sample_values = [7, -4, 9, 0, -5]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")