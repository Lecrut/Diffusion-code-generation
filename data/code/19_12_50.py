def is_even(n):
    return n & 1 == 0

if __name__ == '__main__':
    sample_values = [-7, -5, -3, -1, 0, 1, 3, 5, 7, 9]
    results = {value: is_even(value) for value in sample_values}
    print(results)