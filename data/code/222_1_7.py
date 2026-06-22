def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_smallest(sample_list))