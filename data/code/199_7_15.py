def intersect_names(list1, list2):
    set1 = {name.lower() for name in list1}
    common = [name for name in list2 if name.lower() in set1]
    return common
if __name__ == '__main__':
    sample_list1 = ['Alice', 'Bob', 'Charlie']
    sample_list2 = ['alice', 'Dave', 'bob']
    result = intersect_names(sample_list1, sample_list2)
    print(result)