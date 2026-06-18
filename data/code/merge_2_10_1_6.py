def filter_positive_values(data):
    filtered = {k: v for k, v in data.items() if isinstance(v, (int, float)) and v > 0}
    return dict(sorted(filtered.items()))
if __name__ == '__main__':
    sample_data = {'a': -5, 'b': 10.5, 'c': 3, 'd': 0, 'e': -2.7}
    result = filter_positive_values(sample_data)
    print(result)