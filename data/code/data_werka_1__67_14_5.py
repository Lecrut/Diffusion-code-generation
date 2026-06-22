def find_pair_with_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (complement, num)
        num_map[num] = index
    raise ValueError("No two distinct elements add up to the target value.")

if __name__ == '__main__':
    sample_list = [3, 5, -4, 8, 11, 1, -1, 6]
    target_value = 10
    try:
        result = find_pair_with_sum(sample_list, target_value)
        print(result)
    except ValueError as e:
        print(e)