def filter_positive_values(data):
    filtered = {k: v for k, v in data.items() if isinstance(v, (int, float)) and v > 0}
    sorted_data = dict(sorted(filtered.items(), key=lambda item: item[1], reverse=True))
    return sorted_data
if __name__ == '__main__':
    sample_dict = {
        'apple': -5,
        'banana': 3.2,
        'cherry': 0,
        'date': 7,
        'elderberry': -1.5
    }
    result = filter_positive_values(sample_dict)
    print(result)