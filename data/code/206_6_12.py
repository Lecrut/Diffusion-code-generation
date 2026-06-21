def find_smallest(lst):
    if not lst:
        raise ValueError("List is empty")
    smallest = lst[0]
    for item in lst[1:]:
        if item < smallest:
            smallest = item
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_smallest(sample_list))