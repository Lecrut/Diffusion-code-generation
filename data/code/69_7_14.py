def get_sublist(main_list, start_index, end_index):
    return main_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    start = 1
    end = 4
    print(get_sublist(sample_list, start, end))