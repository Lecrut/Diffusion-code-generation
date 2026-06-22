MAX_KEY = 'max_key'
MAX_VALUE = 'max_value'

def find_max_in_dict(input_dict):
    max_pair = (None, None)
    for key, value in input_dict.items():
        if max_pair[1] is None or value > max_pair[1]:
            max_pair = (key, value)
    return {MAX_KEY: max_pair[0], MAX_VALUE: max_pair[1]}

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 7, 'c': 2, 'd': 9}
    result = find_max_in_dict(sample_dict)
    print(f"Key: {result[MAX_KEY]}, Value: {result[MAX_VALUE]}")