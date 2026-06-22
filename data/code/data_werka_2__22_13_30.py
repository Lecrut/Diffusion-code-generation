def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [10, 15, -7, 8, -3, 0]
    results = {value: is_odd(value) for value in sample_values}
    for value, result in results.items():
        print(f"{value} is odd: {result}")