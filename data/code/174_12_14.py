def invert_dictionary(input_dict):
    inverted = {}
    for key, value in input_dict.items():
        if value not in inverted:
            inverted[value] = key
    return inverted

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    print(invert_dictionary(sample_dict))