def find_two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (nums[left], nums[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5, 6]
    target_value = 9
    result = find_two_sum(sample_array, target_value)
    print(result)