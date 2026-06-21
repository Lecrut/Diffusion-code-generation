def intersect_names(list1, list2):
    set1 = {name.lower() for name in list1}
    common = [name for name in list2 if name.lower() in set1]
    return common

if __name__ == '__main__':
    names_list1 = ['Alice', 'Bob', 'Charlie']
    names_list2 = ['bob', 'dave', 'charlie']
    result = intersect_names(names_list1, names_list2)
    print(result)