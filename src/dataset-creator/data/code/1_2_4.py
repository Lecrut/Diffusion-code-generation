def is_strictly_increasing(nums):
    if len(nums) < 2:
        return True
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    result = is_strictly_increasing(sample_list)
    print(result)