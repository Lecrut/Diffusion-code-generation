def find_smallest_element(lst):
    if not lst:
        raise ValueError("List is empty")
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, 90, 23, 67]
    print(find_smallest_element(sample_list))