def get_middle_value(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    mid_index = length // 2
    if length % 2 == 0:
        val1 = sorted_lst[mid_index - 1]
        val2 = sorted_lst[mid_index]
        return (val1 + val2) / 2
    else:
        return sorted_lst[mid_index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_data)
    print(result)