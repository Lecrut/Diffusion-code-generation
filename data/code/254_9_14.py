def find_second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    
    smallest = second_smallest = float('inf')
    
    for num in lst:
        if num <= smallest:
            smallest, second_smallest = num, smallest
        elif num < second_smallest:
            second_smallest = num
    
    return second_smallest

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 4]
    print(find_second_smallest(sample_list))