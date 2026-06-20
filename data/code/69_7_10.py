def get_sublist(full_list, start_index, end_index):
    return full_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25, 30, 35]
    sub_data = get_sublist(sample_data, 1, 4)
    print(sub_data)