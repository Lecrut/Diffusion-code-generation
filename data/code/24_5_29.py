def is_strictly_less_than_zero(num):
    return num < 0

if __name__ == '__main__':
    sample_values = [-1.5, -0.0, 0.0, 2.3, -1e-10, 1e-10]
    results = {val: is_strictly_less_than_zero(val) for val in sample_values}
    print(results)