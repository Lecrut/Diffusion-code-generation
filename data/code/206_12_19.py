def find_minimum(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    
    minimum = lst[0]
    for item in lst[1:]:
        if item < minimum:
            minimum = item
    
    return minimum

if __name__ == '__main__':
    sample_list_1 = [5, 2, 8, 1, 9]
    min1 = find_minimum(sample_list_1)
    print(f"Minimum of {sample_list_1} is: {min1}")
    
    sample_list_2 = [-10, 0, -5, 3]
    min2 = find_minimum(sample_list_2)
    print(f"Minimum of {sample_list_2} is: {min2}")