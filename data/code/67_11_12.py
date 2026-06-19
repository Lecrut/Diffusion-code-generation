def find_pair_with_sum(arr, target):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input must be a list of integers.")
    left, right = 0, len(arr) - 1
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
    sample_array = [5, 7, 9, 11, 13]
    target_value = 20
    result = find_pair_with_sum(sample_array, target_value)
    print(result)