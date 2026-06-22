def max_min_difference(nums):
    if not nums:
        return 0
    return max(nums) - min(nums)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(max_min_difference(sample_values))