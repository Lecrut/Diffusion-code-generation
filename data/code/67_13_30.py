def find_pair_with_sum(nums, target):
    COMPLEMENT_SET = set()
    for num in nums:
        complement = target - num
        if complement in COMPLEMENT_SET:
            return (complement, num)
        COMPLEMENT_SET.add(num)
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    SAMPLE_LIST = [3, 1, 5, 7, 4]
    TARGET_SUM = 8
    try:
        result = find_pair_with_sum(SAMPLE_LIST, TARGET_SUM)
        print(result)
    except ValueError as e:
        print(e)