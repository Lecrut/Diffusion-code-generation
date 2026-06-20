def find_middle_value(nums):
    if not nums:
        return None

    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]

if __name__ == '__main__':
    sample_values = [3, 5, 2, 4, 6, 0, 1]
    print(find_middle_value(sample_values))