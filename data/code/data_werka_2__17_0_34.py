def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, -4, 5]
    results = {value: is_even(value) for value in sample_values}
    print(results)