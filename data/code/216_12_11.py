def find_median(nums):
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(find_median(data))