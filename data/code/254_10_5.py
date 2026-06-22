def find_min_element(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min_element(sample_list))