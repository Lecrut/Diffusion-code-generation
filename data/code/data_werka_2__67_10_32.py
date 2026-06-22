def find_pair_with_sum(arr, target):
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
    raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0, 1, 2, 3, 4, 5]
    target_value = 8
    result = find_pair_with_sum(sample_array, target_value)
    print(result)