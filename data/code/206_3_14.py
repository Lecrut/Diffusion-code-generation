def find_min(lst):
    if not lst:
        raise ValueError("List is empty")
    
    min_item = lst[0]
    for item in lst[1:]:
        if item < min_item:
            min_item = item
    
    return min_item

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min(sample_list))