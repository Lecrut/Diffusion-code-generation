def find_difference(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

if __name__ == '__main__':
    sample_values = {
        'list1': [10, 20, 30, 40, 50],
        'list2': [30, 40, 50, 60, 70]
    }
    result = find_difference(sample_values['list1'], sample_values['list2'])
    print(result)