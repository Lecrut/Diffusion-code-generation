def second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    
    first, second = float('inf'), float('inf')
    
    for num in lst:
        if num <= first:
            first, second = num, first
        elif num < second:
            second = num
    
    return second

if __name__ == '__main__':
    sample_list = [34, 12, 56, 78, 90, 12]
    print(second_smallest(sample_list))