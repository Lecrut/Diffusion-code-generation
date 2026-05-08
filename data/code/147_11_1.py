def sort_list(input_list):
    return sorted(input_list)
if __name__ == '__main__':
    sample_list_1 = [5, 2, 8, 1, 9]
    sorted_list_1 = sort_list(sample_list_1)
    print(sorted_list_1)
    sample_list_2 = [3.14, 1.618, 2.718]
    sorted_list_2 = sort_list(sample_list_2)
    print(sorted_list_2)
    sample_list_3 = [10, 4, 1, 7, 2]
    sorted_list_3 = sort_list(sample_list_3)
    print(sorted_list_3)
    sample_list_4 = []
    sorted_list_4 = sort_list(sample_list_4)
    print(sorted_list_4)