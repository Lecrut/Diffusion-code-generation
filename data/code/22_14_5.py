def filter_odd_numbers(data):
    return [x for x in data if x % 2 != 0]
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_1 = filter_odd_numbers(sample_list_1)
    print(result_1)
    sample_list_2 = [2, 4, 6, 8, 10]
    result_2 = filter_odd_numbers(sample_list_2)
    print(result_2)
    sample_list_3 = [11, 22, 33, 44, 55]
    result_3 = filter_odd_numbers(sample_list_3)
    print(result_3)
    sample_list_4 = []
    result_4 = filter_odd_numbers(sample_list_4)
    print(result_4)
    sample_list_5 = [1, 3, 5, 7]
    result_5 = filter_odd_numbers(sample_list_5)
    print(result_5)