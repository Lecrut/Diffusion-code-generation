def count_occurrences(dictionary):
    occurrences = {}
    for item in dictionary.values():
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'a': 'apple', 'b': 'banana', 'c': 'apple', 'd': 'orange', 'e': 'banana'}
    print(count_occurrences(sample_dict))