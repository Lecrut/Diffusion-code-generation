def count_occurrences(dictionary):
    occurrences = {}
    for key, value in dictionary.items():
        if value not in occurrences:
            occurrences[value] = 0
        occurrences[value] += 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'a': 'apple', 'b': 'banana', 'c': 'apple', 'd': 'cherry', 'e': 'banana'}
    print(count_occurrences(sample_dict))