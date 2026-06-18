def filter_positive_values(data):
    filtered = {k: v for k, v in data.items() if isinstance(v, (int, float)) and v > 0}
    sorted_data = dict(sorted(filtered.items(), key=lambda item: -item[1]))
    return sorted_data
if __name__ == '__main__':
    sample_dict = {
        "apple": 50.24,
        "banana": -3.76,
        "cherry": 89.12,
        "date": 0,
        "elderberry": 2.34
    }
    result = filter_positive_values(sample_dict)
    print(result)