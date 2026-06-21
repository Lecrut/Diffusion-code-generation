def find_smallest_element(lst):
    if not lst:
        return None
    smallest = min(lst[0], lst[-1])
    for element in lst[2:]:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_smallest_element(sample_list))