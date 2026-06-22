def find_pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9]
    target_value = 8
    result = find_pair_with_target_sum(sample_array, target_value)
    print(result)