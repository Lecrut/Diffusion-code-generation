def count_occurrences(data):
    occurrences = {}
    for key, value in data.items():
        if value not in occurrences:
            occurrences[value] = 0
        occurrences[value] += 1
    return occurrences

if __name__ == '__main__':
    sample_dict = {'x': 'apple', 'y': 'banana', 'z': 'apple', 'w': 'orange', 'v': 'banana'}
    result = count_occurrences(sample_dict)
    print(result)