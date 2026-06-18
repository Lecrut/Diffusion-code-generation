def filter_positive_values(data):
    filtered = {}
    for key in data:
        if isinstance(data[key], (int, float)) and data[key] > 0:
            filtered[key] = data[key]
    sorted_data = dict(sorted(filtered.items()))
    return sorted_data
if __name__ == '__main__':
    sample_dict = {1: -5, 2: 3.5, 3: 0, 4: 7, 5: 2}
    result = filter_positive_values(sample_dict)
    print(result)