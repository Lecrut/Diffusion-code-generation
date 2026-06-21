def invert_dict(original_dict):
    if not all(isinstance(value, hash) for value in original_dict.values()):
        raise ValueError("All values must be hashable.")
    return {value: key for key, value in original_dict.items()}

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 12
    }
    inverted_dict = invert_dict(sample_dict)
    print(inverted_dict)