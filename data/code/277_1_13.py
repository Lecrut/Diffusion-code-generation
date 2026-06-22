def count_occurrences(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    occurrences = {}
    for key, value in data.items():
        if not isinstance(value, (int, str)):
            continue
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'a': 'apple', 'b': 'banana', 'c': 'apple', 'd': 3, 'e': 'banana'}
    print(count_occurrences(sample_dict))