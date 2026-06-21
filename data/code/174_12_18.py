def invert_dict(input_dict):
    inverted = {v: k for k, v in input_dict.items()}
    return inverted

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    print(invert_dict(sample_dict))