def count_matching_elements(arr1, arr2, positions):
    return sum(1 for pos in positions if arr1[pos] == arr2[pos])

if __name__ == '__main__':
    sample_arr1 = [10, 20, 30, 40, 50]
    sample_arr2 = [10, 25, 30, 45, 50]
    sample_positions = [0, 2, 4]
    print(count_matching_elements(sample_arr1, sample_arr2, sample_positions))