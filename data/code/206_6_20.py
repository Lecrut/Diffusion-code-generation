def find_smallest_element(lst):
    if not lst:
        return None
    smallest = lst[0]
    for element in lst[1:]:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1, 9]
    print(find_smallest_element(sample_list))