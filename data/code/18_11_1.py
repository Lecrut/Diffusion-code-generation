def get_middle_value(lst):
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_middle_value(sample_list))