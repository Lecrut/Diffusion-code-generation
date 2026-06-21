def get_middle_value(lst):
    if not lst:
        return None
    if len(lst) % 2 == 0:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_value(sample_list)
    print(result)