def invert_dictionary(input_dict):
    return {v: k for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    inverted_dict = invert_dictionary(sample_dict)
    print(inverted_dict)