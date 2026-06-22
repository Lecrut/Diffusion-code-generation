def get_first_last_middle(nums):
    if not nums:
        return ()
    first = nums[0]
    last = nums[-1]
    middle_index = len(nums) // 2
    middle = nums[middle_index]
    return (first, last, middle)

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45, 55]
    result = get_first_last_middle(sample_list)
    print(result)