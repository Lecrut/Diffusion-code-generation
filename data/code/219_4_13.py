def find_max_value(dictionary):
    max_key = None
    max_value = float('-inf')
    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}
    print("Sample Dictionary:", sample_dict)
    result_key, result_value = find_max_value(sample_dict)
    print(f"Key with Maximum Value: {result_key}, Maximum Value: {result_value}")