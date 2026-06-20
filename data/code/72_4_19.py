def merge_lists_at_index(list1, list2, index):
    result = []
    for i in range(min(len(list1), len(list2))):
        if i == index:
            result.append((list1[i], list2[i]))
    return result

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = ['a', 'b', 'c', 'd', 'e']
    sample_index = 2
    print(merge_lists_at_index(sample_list1, sample_list2, sample_index))