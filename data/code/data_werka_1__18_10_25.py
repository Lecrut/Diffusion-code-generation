def first_greater_than_second(lst):
    return lst[0] > lst[1]
if __name__ == '__main__':
    sample_list1 = [10, 5]
    print(first_greater_than_second(sample_list1))
    sample_list2 = [3, 7]
    print(first_greater_than_second(sample_list2))
    sample_list3 = [10.5, 10.5]
    print(first_greater_than_second(sample_list3))
    sample_list4 = [-2, -5]
    print(first_greater_than_second(sample_list4))