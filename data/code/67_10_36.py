def find_two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    raise ValueError("No two elements sum up to the target")

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5, 6]
    target_value = 9
    result = find_two_sum(sample_array, target_value)
    print(result)