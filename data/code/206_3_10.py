def find_min(lst):
    if not lst:
        return None
    min_item = lst[0]
    for item in lst[1:]:
        if item < min_item:
            min_item = item
    return min_item

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min(sample_list))