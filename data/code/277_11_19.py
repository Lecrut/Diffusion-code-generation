def count_items(dictionary):
    counts = {}
    for item in dictionary.values():
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    print(count_items(sample_dict))