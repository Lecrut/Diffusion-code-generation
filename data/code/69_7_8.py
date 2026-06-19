def get_sublist(large_list, start_index, end_index):
    return large_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    start = 2
    end = 5
    sub_list = get_sublist(sample_list, start, end)
    print(sub_list)