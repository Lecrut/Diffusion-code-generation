def find_smallest_missing_positive(nums):
    n = len(nums)
    if 1 not in nums:
        return 1
    
    contains_one = False
    for i in range(n):
        if nums[i] == 1:
            contains_one = True
            break
    if not contains_one:
        return 1
    
    nums = [0] + nums
    n += 1
    
    for i in range(1, n):
        while 1 <= nums[i] <= n and nums[nums[i]] != nums[i]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    
    for i in range(1, n):
        if nums[i] != i:
            return i
    
    return n

if __name__ == '__main__':
    sample_values = [3, 4, -1, 1]
    print(find_smallest_missing_positive(sample_values))