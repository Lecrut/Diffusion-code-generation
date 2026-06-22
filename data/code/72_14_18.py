def count_matching_elements(arr1, arr2, positions):
    count = 0
    for pos in positions:
        if pos < 0 or pos >= len(arr1) or pos >= len(arr2):
            raise ValueError(f"Position {pos} is out of bounds for one or both arrays.")
        if arr1[pos] == arr2[pos]:
            count += 1
    return count

if __name__ == '__main__':
    sample_arr1 = [10, 20, 30, 40, 50]
    sample_arr2 = [10, 25, 30, 45, 55]
    sample_positions = [0, 1, 2, 3, 4]
    result = count_matching_elements(sample_arr1, sample_arr2, sample_positions)
    print(result)