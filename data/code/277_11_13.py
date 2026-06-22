def count_occurrences(dictionary):
    occurrences = {}
    for item in dictionary.values():
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    print(count_occurrences(sample_dict))