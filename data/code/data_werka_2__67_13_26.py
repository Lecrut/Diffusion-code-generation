def find_pair_with_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return (complement, num)
        num_to_index[num] = index
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    SAMPLE_LIST = [3, 5, -4, 8, 11, 1, -1, 6]
    TARGET_SUM = 10
    try:
        result = find_pair_with_sum(SAMPLE_LIST, TARGET_SUM)
        print(result)
    except ValueError as e:
        print(e)