def find_two_sum(arr, target):
    left_index = 0
    right_index = len(arr) - 1
    
    while left_index < right_index:
        current_pair_sum = arr[left_index] + arr[right_index]
        
        if current_pair_sum == target:
            return (arr[left_index], arr[right_index])
        elif current_pair_sum < target:
            left_index += 1
        else:
            right_index -= 1
    
    raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0, 3, 5, 7, 9, 12]
    target_value = 14
    result_pair = find_two_sum(sample_array, target_value)
    print(result_pair)