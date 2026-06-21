def intersect_names(list1, list2):
    set1 = {name.lower() for name in list1}
    common_names = [name for name in list2 if name.lower() in set1]
    return common_names

if __name__ == '__main__':
    names_list1 = ['Alice', 'Bob', 'Charlie']
    names_list2 = ['bob', 'david', 'alice']
    print(intersect_names(names_list1, names_list2))