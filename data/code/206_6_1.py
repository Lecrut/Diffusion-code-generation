def find_smallest_element(lst):
    smallest = lst[0]
    for element in lst:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_smallest_element(sample_list))