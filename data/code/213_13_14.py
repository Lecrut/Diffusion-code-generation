def find_kth_smallest(nums, k):

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

    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)
    import random
    return select(0, len(nums) - 1, k - 1)
if __name__ == '__main__':
    sample_nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_smallest(sample_nums, k))
    sample_nums = [9, 7, 8, 3, 2, 10, 6]
    k = 4
    print(find_kth_smallest(sample_nums, k))