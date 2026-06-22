def is_odd(n):
    return n & 1 != 0

if __name__ == '__main__':
    sample_values = [42, 73, -15, 0, 256]
    results = {value: is_odd(value) for value in sample_values}
    print(results)