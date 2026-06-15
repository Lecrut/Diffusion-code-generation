def match_and_sort(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, str):
            result[key] = value
    return sorted(result.keys())
if __name__ == '__main__':
    sample_data = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange",
        "kiwi": 123,
        "melon": "green"
    }
    sorted_keys = match_and_sort(sample_data)
    print(sorted_keys)