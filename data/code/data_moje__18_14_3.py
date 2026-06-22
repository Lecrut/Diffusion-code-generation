def get_middle_value(lst):
    if not lst:
        raise ValueError("List must not be empty")
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_value(sample_list)
    print(result)