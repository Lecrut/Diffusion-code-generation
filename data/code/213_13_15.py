def kth_smallest(nums, k):
    if len(nums) == 1:
        return nums[0]
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    if k <= len(left):
        return kth_smallest(left, k)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return kth_smallest(right, k - len(left) - len(middle))
if __name__ == '__main__':
    print(kth_smallest([3, 2, 1, 5, 6, 4], 2))
    print(kth_smallest([7, 10, 4, 3, 20, 15], 3))