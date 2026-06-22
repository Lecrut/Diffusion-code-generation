MAX_VALUE = float('-inf')

def find_max_value(dictionary):
    max_key = None
    for key, value in dictionary.items():
        if value > MAX_VALUE:
            MAX_VALUE = value
            max_key = key
    return max_key, MAX_VALUE

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 10, 'c': 5, 'd': 20}
    print("Key with maximum value:", find_max_value(sample_dict)[0])
    print("Maximum value:", find_max_value(sample_dict)[1])