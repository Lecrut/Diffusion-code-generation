def are_sums_different(list1, list2):
    sum1 = 0
    sum2 = 0
    
    for num in list1:
        sum1 += num
    
    for num in list2:
        sum2 += num
    
    return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [7, 8, 9, 10]
    sample_list2 = [3, 4, 5, 6]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)