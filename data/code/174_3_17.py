def validate_dict(d):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary")
    if len(d) != len(set(d.values())):
        raise ValueError("All values in the dictionary must be unique")

def invert_dictionary(input_dict):
    validate_dict(input_dict)
    return {v: k for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
    inverted_dict = invert_dictionary(sample_dict)
    print(inverted_dict)