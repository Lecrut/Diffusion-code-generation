def count_non_dictionaries(data):
    non_dict_count = 0
    for item in data:
        if not isinstance(item, dict):
            non_dict_count += 1
    return non_dict_count

if __name__ == '__main__':
    list1 = [1, {'a': 2}, '3', {}, [], (4,)]
    list2 = [{'b': 2}, {'c': 3}]
    list3 = ['string', 42, None]
    print(f"List 1: {count_non_dictionaries(list1)}")
    print(f"List 2: {count_non_dictionaries(list2)}")
    print(f"List 3: {count_non_dictionaries(list3)}")