def find_pair_with_sum(arr, target):
    LEFT_POINTER_START = 0
    RIGHT_POINTER_START = len(arr) - 1
    
    left = LEFT_POINTER_START
    right = RIGHT_POINTER_START
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0, 5, 8, 13, 19, 24]
    target_value = 32
    result = find_pair_with_sum(sample_array, target_value)
    print(result)