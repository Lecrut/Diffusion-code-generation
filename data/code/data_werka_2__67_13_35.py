def find_pair_with_sum(nums, target):
    num_set = set()
    for num in nums:
        complement = target - num
        if complement in num_set:
            return (complement, num)
        num_set.add(num)
    raise ValueError("No two distinct elements add up to the target sum.")

if __name__ == '__main__':
    sample_list = [2, 7, 11, 15]
    target_sum = 9
    try:
        result = find_pair_with_sum(sample_list, target_sum)
        print(result)
    except ValueError as e:
        print(e)