def is_positive(n):
    return n > 0

if __name__ == '__main__':
    sample_values = [1, -1, 0, 42, -42]
    results = {value: is_positive(value) for value in sample_values}
    print(results)