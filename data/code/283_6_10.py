def count_non_dictionaries(data):
    non_dict_count = sum(not isinstance(x, dict) for x in data)
    return non_dict_count

if __name__ == '__main__':
    list1 = [1, 5, 10, 2]
    list2 = [1, 5, -3, 2]
    list3 = [10, 20, 30]
    list4 = [-1, 5, 10]
    
    print(f"List 1: {count_non_dictionaries(list1)}")
    print(f"List 2: {count_non_dictionaries(list2)}")
    print(f"List 3: {count_non_dictionaries(list3)}")
    print(f"List 4: {count_non_dictionaries(list4)}")