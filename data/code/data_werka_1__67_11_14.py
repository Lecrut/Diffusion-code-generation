def validate_input(arr, target):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input array must be a list of integers.")
    if not isinstance(target, int):
        raise ValueError("Target must be an integer.")

def find_two_sum_with_validation(arr, target):
    validate_input(arr, target)
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == '__main__':
    sample_array = [2, 5, 8, 14, 18, 20]
    target_value = 32
    result = find_two_sum_with_validation(sample_array, target_value)
    print(result)