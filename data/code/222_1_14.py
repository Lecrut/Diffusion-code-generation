def find_smallest(lst):
    if not lst:
        raise ValueError("Input list is empty")
    
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_smallest(sample_list))