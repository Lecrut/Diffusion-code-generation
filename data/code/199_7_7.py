def intersect_names(list1, list2):
    set1 = {name.lower() for name in list1}
    common = [name for name in list2 if name.lower() in set1]
    return common
if __name__ == '__main__':
    names1 = ['Alice', 'Bob', 'Charlie']
    names2 = ['bob', 'dave', 'Eve']
    result = intersect_names(names1, names2)
    print(result)