def count_occurrences(dictionary):
    occurrences = {}
    for key, value in dictionary.items():
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 1}
    print(count_occurrences(sample_dict))