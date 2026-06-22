def find_element_differences(list1, list2):
    return [abs(a - b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_data = {
        'list_a': [1, 5, 10, 15],
        'list_b': [3, 7, 8, 12]
    }
    result = find_element_differences(sample_data['list_a'], sample_data['list_b'])
    print(result)