def get_median(nums):
    if not nums:
        raise ValueError("List cannot be empty")
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid_index = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid_index - 1] + sorted_nums[mid_index]) // 2
    return sorted_nums[mid_index]

if __name__ == '__main__':
    list_a = [3, 1, 4, 1, 5, 9, 2]
    list_b = [10, 20, 30, 40]
    print(get_median(list_a))
    print(get_median(list_b))