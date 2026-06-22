def is_positive(value):
    return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    samples = [10, -5, 0, 3.14, -2.71, 'string', None]
    results = {sample: is_positive(sample) for sample in samples}
    print(results)