def find_smallest(lst):
    if not lst:
        raise ValueError("Input list cannot be empty")
    
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_list = [12, 45, 78, -3, 0, 1]
    print(find_smallest(sample_list))