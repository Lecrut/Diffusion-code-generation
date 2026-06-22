def find_median(nums):
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 8, 9, 15]
    print(find_median(sample_list))