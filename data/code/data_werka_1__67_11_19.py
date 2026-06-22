def find_pair_with_sum_sorted(arr, target):
    left_index = 0
    right_index = len(arr) - 1
    
    while left_index < right_index:
        current_sum = arr[left_index] + arr[right_index]
        
        if current_sum == target:
            return (arr[left_index], arr[right_index])
        elif current_sum < target:
            left_index += 1
        else:
            right_index -= 1
    
    return None

if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value = 16
    result_pair = find_pair_with_sum_sorted(sample_array, target_value)
    print(result_pair)