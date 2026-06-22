def find_min(nums):
    if not nums:
        raise ValueError("List must not be empty")
    current_min = nums[0]
    for num in nums[1:]:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_list = [34, -1, 23, 7, -15, 0, 12]
    result = find_min(sample_list)
    print(result)