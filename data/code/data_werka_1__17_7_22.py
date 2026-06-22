def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [42, 7, 0, -3, 100]
    results = {value: is_even(value) for value in sample_values}
    print(results)