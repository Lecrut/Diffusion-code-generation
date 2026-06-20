def count_matching_elements(arr1, arr2):
    match_count = 0
    n = min(len(arr1), len(arr2))
    for i in range(n):
        if arr1[i] == arr2[i]:
            match_count += 1
    return match_count

if __name__ == '__main__':
    sample_array1 = [1, 2, 3, 4, 5, 6]
    sample_array2 = [1, 3, 3, 4, 0, 6]
    result = count_matching_elements(sample_array1, sample_array2)
    print(result)