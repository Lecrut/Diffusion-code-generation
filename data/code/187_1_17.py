def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4, 8, 7, 6]
    print(find_max(sample_list))