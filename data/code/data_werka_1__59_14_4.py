def find_middle_value(nums):
    nums.sort()
    return nums[len(nums) // 2]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    middle_value = find_middle_value(sample_values)
    print(middle_value)