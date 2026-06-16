def filter_positive_values(data):
    return {k: v for k, v in data.items() if isinstance(v, (int, float)) and v > 0}
if __name__ == '__main__':
    sample_data = {'a': -5, 'b': 10, 'c': 3.5, 'd': 0, 'e': -2}
    filtered_and_sorted = dict(sorted(filter_positive_values(sample_data).items()))
    print(filtered_and_sorted)