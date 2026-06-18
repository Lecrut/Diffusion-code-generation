def filter_positive_values(data):
    filtered = {k: v for k, v in data.items() if isinstance(v, (int, float)) and v > 0}
    sorted_data = dict(sorted(filtered.items()))
    return sorted_data
if __name__ == '__main__':
    sample_dict = {'a': -5, 'b': 10, 'c': 3.5, 'd': 0, 'e': -2}
    result = filter_positive_values(sample_dict)
    print(result)