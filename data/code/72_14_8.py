def count_matching_elements(arr1, arr2, positions):
    return sum(1 for pos in positions if arr1[pos] == arr2[pos])

if __name__ == '__main__':
    array1 = [10, 20, 30, 40, 50]
    array2 = [10, 25, 30, 45, 50]
    positions_to_check = [0, 2, 4]
    
    result = count_matching_elements(array1, array2, positions_to_check)
    print(result)