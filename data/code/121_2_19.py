def longer_list(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    if size1 > size2:
        return list1
    elif size2 > size1:
        return list2
    else:
        return None
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8, 9]
    result = longer_list(sample_list1, sample_list2)
    print(result)