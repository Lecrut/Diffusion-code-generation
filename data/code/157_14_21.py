def find_smallest(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_smallest(sample_values))