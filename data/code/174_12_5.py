def invert_dictionary(original_dict):
    inverted_dict = {v: k for k, v in original_dict.items()}
    return inverted_dict

if __name__ == '__main__':
    sample_dict = {
        "apple": 1,
        "banana": 2,
        "orange": 3
    }
    print(invert_dictionary(sample_dict))