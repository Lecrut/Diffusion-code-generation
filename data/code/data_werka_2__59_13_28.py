def find_middle_value(nums):
    if len(nums) == 0:
        raise ValueError("The list is empty")
    nums.sort()
    mid_index = len(nums) // 2
    return nums[mid_index]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    middle_value = find_middle_value(sample_values)
    print(middle_value)