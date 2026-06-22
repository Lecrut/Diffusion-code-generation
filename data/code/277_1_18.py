def count_occurrences(data):
    occurrences = {}
    for item in data:
        if item not in occurrences:
            occurrences[item] = 0
        occurrences[item] += 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'apple': 3, 'banana': 2, 'orange': 5}
    print(count_occurrences(sample_dict))