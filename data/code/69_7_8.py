def get_sublist(lst, start_index, end_index):
    return lst[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_sublist(sample_list, 1, 3))