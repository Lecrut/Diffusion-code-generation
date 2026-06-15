def match_and_sort(data):
    result = {}
    for key, value in data.items():
        result[key] = value
    sorted_keys = sorted(result.keys())
    return sorted_keys
if __name__ == '__main__':
    sample_dict = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red",
        "date": "brown"
    }
    sorted_keys = match_and_sort(sample_dict)
    print(sorted_keys)