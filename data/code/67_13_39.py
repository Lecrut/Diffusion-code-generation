def find_pair_with_sum(nums, target):
    COMPLEMENT_MAP = {}
    for num in nums:
        complement = target - num
        if complement in COMPLEMENT_MAP:
            return (complement, num)
        COMPLEMENT_MAP[num] = True
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    SAMPLE_LIST = [5, 3, -4, 8, 11, 1, -1, 6]
    TARGET_SUM = 10
    try:
        result = find_pair_with_sum(SAMPLE_LIST, TARGET_SUM)
        print(result)
    except ValueError as e:
        print(e)