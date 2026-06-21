def intersect_names(list1, list2):
    set1 = {name.lower() for name in list1}
    common_names = [name for name in list2 if name.lower() in set1]
    return common_names

if __name__ == '__main__':
    sample_list1 = ['Alice', 'Bob', 'Charlie']
    sample_list2 = ['bob', 'dave', 'charlie']
    print(intersect_names(sample_list1, sample_list2))