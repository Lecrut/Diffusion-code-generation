def count_items(dictionary):
    occurrences = {}
    for key, value in dictionary.items():
        if value not in occurrences:
            occurrences[value] = 0
        occurrences[value] += 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    print(count_items(sample_dict))