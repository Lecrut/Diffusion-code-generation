def invert_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    inverted = {}
    for key, value in input_dict.items():
        if not isinstance(value, hashable):
            raise ValueError("All values in the dictionary must be hashable")
        if value in inverted:
            raise ValueError("Dictionary values must be unique")
        inverted[value] = key
    
    return inverted

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    try:
        result = invert_dict(sample_dict)
        print(result)
    except ValueError as e:
        print(e)