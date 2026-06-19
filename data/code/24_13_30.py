def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.5, 2]
    results = {val: is_negative(val) for val in sample_values}
    print(results)