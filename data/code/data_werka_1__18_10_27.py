def is_first_greater_than_second(lst):
    return lst[0] > lst[1]
if __name__ == '__main__':
    sample_list_1 = [15, 10]
    sample_list_2 = [4.5, 4.6]
    sample_list_3 = [-2, -3]
    print(is_first_greater_than_second(sample_list_1))
    print(is_first_greater_than_second(sample_list_2))
    print(is_first_greater_than_second(sample_list_3))