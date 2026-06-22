def find_pair_sum(nums, target):
    NUM_TYPE_ERROR_MSG = "nums must be a list of integers"
    TARGET_TYPE_ERROR_MSG = "target must be an integer"
    
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError(NUM_TYPE_ERROR_MSG)
    if not isinstance(target, int):
        raise ValueError(TARGET_TYPE_ERROR_MSG)
    
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError("No two sum solution")

if __name__ == '__main__':
    SAMPLE_NUMS = [10, 15, 3, 7]
    TARGET_VALUE = 17
    result = find_pair_sum(SAMPLE_NUMS, TARGET_VALUE)
    print(result)