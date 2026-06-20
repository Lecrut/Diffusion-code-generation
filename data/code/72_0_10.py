def compare_elements(list1, list2, index):
    try:
        return list1[index], list2[index]
    except IndexError:
        return None, None

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = ['a', 'b', 'c']
    index_to_compare = 1
    result = compare_elements(sample_list1, sample_list2, index_to_compare)
    print(result)