def count_matching_elements(arr1, arr2, indices):
    count = 0
    for idx in indices:
        if idx < len(arr1) and idx < len(arr2):
            if arr1[idx] == arr2[idx]:
                count += 1
    return count

if __name__ == '__main__':
    sample_arr1 = [10, 20, 30, 40, 50]
    sample_arr2 = [10, 25, 30, 45, 55]
    sample_indices = [0, 2, 4]
    result = count_matching_elements(sample_arr1, sample_arr2, sample_indices)
    print(result)