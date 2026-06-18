def filter_positive_values(data):
    filtered = {k: v for k, v in data.items() if v > 0}
    return dict(sorted(filtered.items()))
if __name__ == '__main__':
    sample_data = {'a': -5, 'b': 10, 'c': 3.5, 'd': 0, 'e': 7}
    result = filter_positive_values(sample_data)
    print(result)