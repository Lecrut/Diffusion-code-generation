def find_min_value(lst):
    if not lst:
        return None
    current_min = lst[0]
    for num in lst[1:]:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_list = [7, 3, 9, 1, 4, 8, 5, 2, 6]
    print(find_min_value(sample_list))