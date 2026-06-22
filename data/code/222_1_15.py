def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [12, 45, 78, 3, 67, 2, 90, 1]
    print(find_smallest(sample_list))