def get_median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) // 2

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5]
    list2 = [10, 20, 30, 40]
    print(get_median(list1))
    print(get_median(list2))