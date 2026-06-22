def is_positive(x):
    return x > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.5, -2.7]
    results = {x: is_positive(x) for x in sample_values}
    print(results)