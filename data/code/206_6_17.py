def find_smallest_element(lst):
    smallest = lst[0]
    for element in lst:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [15, 28, 3, 42, 7, 56]
    print(find_smallest_element(sample_list))