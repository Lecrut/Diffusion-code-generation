def find_kth_smallest(nums, k):
    if not nums or k <= 0:
        return None
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    if k <= len(left):
        return find_kth_smallest(left, k)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return find_kth_smallest(right, k - len(left) - len(middle))
if __name__ == '__main__':
    test_cases = [([3, 2, 1, 5, 6, 4], 2), ([7, 10, 4, 3, 20, 15], 3), ([9, 8, 7, 6, 5, 4, 3, 2, 1], 5), ([1], 1), ([], 1)]
    for nums, k in test_cases:
        result = find_kth_smallest(nums, k)
        print(f'Input: {nums}, k={k} -> Output: {result}')