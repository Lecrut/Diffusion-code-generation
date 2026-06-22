def compare_lists(list1, list2):
    return max((list1, list2), key=sum)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [5, 15, 25, 35]
    result = compare_lists(sample_list1, sample_list2)
    print(result)