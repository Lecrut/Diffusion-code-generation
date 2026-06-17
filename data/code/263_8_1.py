def count_greater_pairs(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] > nums[j]:
                count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    result = count_greater_pairs(sample_list)
    print(result)