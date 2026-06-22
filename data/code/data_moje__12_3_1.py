def find_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    if len(lst) % 2 == 0:
        return [lst[mid_index - 1], lst[mid_index]]
    else:
        return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = find_middle_element(sample_list)
    print(result)