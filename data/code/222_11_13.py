def find_smallest_element(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 10]
    print(find_smallest_element(sample_list))