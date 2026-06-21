def kth_smallest_element(nums, k):
    if not nums:
        return None
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    if k <= len(left):
        return kth_smallest_element(left, k)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return kth_smallest_element(right, k - len(left) - len(middle))
if __name__ == '__main__':
    test_cases = [([3, 2, 1, 5, 6, 4], 2), ([3, 0, 6, 1, 5, 4], 3), ([9, 8, 7, 6, 5, 4, 3, 2, 1], 5)]
    for nums, k in test_cases:
        result = kth_smallest_element(nums, k)
        print(f'K-th smallest element in {nums} is: {result}')