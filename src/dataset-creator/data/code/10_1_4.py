def filter_positive_dict(data):
    return {k: v for k, v in data.items() if v > 0}
if __name__ == '__main__':
    sample_data = {'a': -5, 'b': 10, 'c': 3.5, 'd': 0, 'e': -2}
    filtered_dict = filter_positive_dict(sample_data)
    sorted_items = dict(sorted(filtered_dict.items()))
    print(f"Filtered and Sorted: {sorted_items}")