def find_pair_with_sum(sorted_array, target):
    left_index = 0
    right_index = len(sorted_array) - 1
    
    while left_index < right_index:
        current_sum = sorted_array[left_index] + sorted_array[right_index]
        
        if current_sum == target:
            return (sorted_array[left_index], sorted_array[right_index])
        elif current_sum < target:
            left_index += 1
        else:
            right_index -= 1
    
    raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0, 2, 3, 5, 7, 8]
    target_value = 10
    result_pair = find_pair_with_sum(sample_array, target_value)
    print(result_pair)