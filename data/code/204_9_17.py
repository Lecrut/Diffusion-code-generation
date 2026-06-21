def median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    return (nums[mid] + nums[~mid]) / 2

if __name__ == '__main__':
    print(median([3, 1, 2, 4, 5]))
    print(median([-10, 4, 6, 1000, 10, 20]))