def find_kth_smallest(nums, k):
    if k < 1 or k > len(nums):
        raise ValueError('k is out of bounds')

    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = (nums[right], nums[pivot_index])
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = (nums[i], nums[store_index])
                store_index += 1
        nums[right], nums[store_index] = (nums[store_index], nums[right])
        return store_index
    left, right = (0, len(nums) - 1)
    while True:
        pivot_index = partition(left, right, right)
        if pivot_index == k - 1:
            return nums[pivot_index]
        elif pivot_index < k - 1:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
if __name__ == '__main__':
    print(find_kth_smallest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_smallest([7, 10, 4, 3, 20, 15], 3))