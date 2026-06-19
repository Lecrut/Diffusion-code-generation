def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, -1, -2, -3]
    results = {value: is_odd(value) for value in sample_values}
    print(results)