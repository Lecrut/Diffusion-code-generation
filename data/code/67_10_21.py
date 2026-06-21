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
    raise ValueError("No two sum solution")

if __name__ == '__main__':
    nums = [-2, 1, 2, 4, 7, 11]
    target = 9
    result = find_two_sum(nums, target)
    print(result)