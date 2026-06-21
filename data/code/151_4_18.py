def zip_lists(list1, list2):
    return list(zip(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    result = zip_lists(sample_list1, sample_list2)
    print(f"Zipped lists {sample_list1} and {sample_list2}: {result}")