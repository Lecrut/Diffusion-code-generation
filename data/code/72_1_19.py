def compare_elements(list1, list2, index):
    if list1[index] > list2[index]:
        return (list1[index], 'greater than', list2[index])
    elif list1[index] < list2[index]:
        return (list1[index], 'less than', list2[index])
    else:
        return (list1[index], 'equal to', list2[index])

if __name__ == '__main__':
    sample_list1 = [5, 3, 9]
    sample_list2 = [4, 6, 8]
    index_to_compare = 1
    result = compare_elements(sample_list1, sample_list2, index_to_compare)
    print(result)