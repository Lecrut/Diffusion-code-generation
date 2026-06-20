def get_sublist(lst, start_idx, end_idx):
    return lst[start_idx:end_idx + 1]

if __name__ == '__main__':
    sample_list = [3, 6, 9, 12, 15, 18, 21]
    sub_list = get_sublist(sample_list, 1, 4)
    print(sub_list)