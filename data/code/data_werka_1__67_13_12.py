def find_zero_sum_pairs(nums):
    nums.sort()
    left, right = 0, len(nums) - 1
    pairs = set()
    
    while left < right:
        if nums[left] + nums[right] == 0:
            pairs.add((nums[left], nums[right]))
            left += 1
            right -= 1
        elif nums[left] + nums[right] < 0:
            left += 1
        else:
            right -= 1
    
    return list(pairs)

if __name__ == '__main__':
    sample_values = [3, -3, 2, -2, 1, -1, 4, -4, 5, -5]
    result = find_zero_sum_pairs(sample_values)
    print(result)