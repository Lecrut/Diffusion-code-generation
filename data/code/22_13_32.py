def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    parity_map = {True: 'Odd', False: 'Even'}
    sample_values = [7, -3, 10, 0, -5, 8]
    for value in sample_values:
        result = is_odd(value)
        print(f"{value} is {parity_map[result]}")