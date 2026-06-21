def find_smallest_element(lst):
    if not lst:
        return None
    smallest = lst[0]
    for element in lst:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [7, 3, 5, 2, 9, 1, 4, 6, 8]
    print(find_smallest_element(sample_list))