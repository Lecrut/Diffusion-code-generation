def match_and_sort(data):
    key_value_pairs = list(data.items())
    sorted_keys = sorted([key for key, value in key_value_pairs])
    return sorted_keys
if __name__ == '__main__':
    sample_dictionary = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange"
    }
    result = match_and_sort(sample_dictionary)
    print(result)