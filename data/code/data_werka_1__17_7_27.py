def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [4, 7, 10, 13, 16]
    results = {value: is_even(value) for value in sample_values}
    print(results)