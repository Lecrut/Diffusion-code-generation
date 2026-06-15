def match_and_sort(data):
    result = {}
    for key, value in data.items():
        if value in ["simple words"]:
            result[key] = value
    return sorted(result.keys())
if __name__ == '__main__':
    sample_data = {
        "apple": "simple words",
        "banana": "complex phrase",
        "cherry": "simple words",
        "date": "another word"
    }
    sorted_keys = match_and_sort(sample_data)
    print(sorted_keys)