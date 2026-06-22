def count_matching_values(arr1, arr2, indices):
    count = 0
    for idx in indices:
        if idx >= len(arr1) or idx >= len(arr2):
            continue
        if arr1[idx] == arr2[idx]:
            count += 1
    return count

if __name__ == '__main__':
    first_array = [100, 200, 300, 400, 500]
    second_array = [100, 250, 300, 450, 600]
    target_indices = [0, 1, 3, 4]
    matches = count_matching_values(first_array, second_array, target_indices)
    print(matches)