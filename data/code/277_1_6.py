def count_occurrences(dictionary):
    counts = {}
    for key, value in dictionary.items():
        if value not in counts:
            counts[value] = 0
        counts[value] += 1
    return counts

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    print(count_occurrences(sample_dict))