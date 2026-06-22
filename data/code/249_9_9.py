def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4, 8, 6, 7]
    print(find_max(sample_list))