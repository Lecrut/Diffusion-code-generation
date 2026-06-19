def sum_lists_differ(list1, list2):
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 4, 3, 2, 1]
    result = sum_lists_differ(sample_list1, sample_list2)
    print(result)