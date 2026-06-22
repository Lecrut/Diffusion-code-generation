def validate_dict(dictionary):
    if not isinstance(dictionary, dict) or not all(isinstance(value, int) for value in dictionary.values()):
        raise ValueError("Input must be a dictionary with integer values.")

def find_min_max(dictionary):
    validate_dict(dictionary)
    min_val = max_val = next(iter(dictionary.values()))
    for value in dictionary.values():
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    min_val, max_val = find_min_max(sample_dict)
    print(f"Minimum value: {min_val}, Maximum value: {max_val}")