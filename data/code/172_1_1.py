def match_keys_to_words(data):
    keys = list(data.keys())
    return keys
if __name__ == '__main__':
    sample_dict = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange"
    }
    result = match_keys_to_words(sample_dict)
    print(result)