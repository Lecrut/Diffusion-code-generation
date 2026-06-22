def are_sums_different(list1, list2):
    if not isinstance(list1, (list, tuple)) or not isinstance(list2, (list, tuple)):
        raise ValueError("Both inputs must be lists or tuples.")
    
    sum1 = 0
    sum2 = 0
    
    for num in list1:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the first list must be numbers.")
        sum1 += num
    
    for num in list2:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the second list must be numbers.")
        sum2 += num
    
    return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [5, 15, 25, 35, 45]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)