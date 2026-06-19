def is_odd(n):
    return (n & 1) != 0

if __name__ == '__main__':
    sample_values = [42, 7, 0, -3, 15]
    results = {value: is_odd(value) for value in sample_values}
    print(results)