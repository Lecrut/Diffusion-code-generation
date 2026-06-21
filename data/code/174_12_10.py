def invert_dict(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
    return inverted_dict

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    inverted_sample = invert_dict(sample_dict)
    print(inverted_sample)