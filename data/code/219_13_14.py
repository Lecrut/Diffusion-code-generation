def find_largest_value(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError("Input must be a dictionary")
    if not dictionary:
        return None
    return max(dictionary.values())

if __name__ == '__main__':
    sample_dict = {'x': 10, 'y': 20, 'z': 5}
    print(find_largest_value(sample_dict))