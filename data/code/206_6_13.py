def find_smallest(lst):
    if not lst:
        raise ValueError("List is empty")
    smallest = lst[0]
    for item in lst[1:]:
        if item < smallest:
            smallest = item
    return smallest

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 4]
    print(find_smallest(sample_list))