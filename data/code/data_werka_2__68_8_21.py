def find_first_zero_difference_index(list_a, list_b):
    for index, value in enumerate(zip(list_a, list_b[:-1])):
        if value[0] - list_b[index + 1] == 0:
            return index
    return -1

if __name__ == '__main__':
    sample_data = {
        'list_a': [1, 3, 5, 7, 9],
        'list_b': [2, 3, 6, 7, 10]
    }
    result = find_first_zero_difference_index(sample_data['list_a'], sample_data['list_b'])
    print(result)