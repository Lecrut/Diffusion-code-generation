def are_sums_different(list1, list2):
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
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [2, 4, 6, 8, 10]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)