def get_sublist(large_list, start_index, end_index):
    return large_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    start = 2
    end = 5
    sub_list = get_sublist(sample_list, start, end)
    print(sub_list)