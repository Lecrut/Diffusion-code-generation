def match_and_sort(data):
    result = {}
    for key, value in data.items():
        if value.isalpha():
            result[key] = value
    return sorted(result.keys())
if __name__ == '__main__':
    sample_data = {
        "apple": "fruit",
        "banana": "color",
        "carrot": "vegetable",
        "grape": "fruit",
        "orange": "color",
        "water": "liquid"
    }
    sorted_keys = match_and_sort(sample_data)
    print(sorted_keys)