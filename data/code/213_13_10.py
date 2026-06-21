def find_kth_smallest(nums, k):
    if not nums or k <= 0:
        return None
    pivot = nums[0]
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
    sample_numbers = [34, 21, 56, 78, 90, 12, 55]
    k = 4
    result = find_kth_smallest(sample_numbers, k)
    print(f"The {k}-th smallest element is: {result}")