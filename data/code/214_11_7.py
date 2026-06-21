def find_min_element(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, 90, 23, 67, 1]
    print(find_min_element(sample_list))