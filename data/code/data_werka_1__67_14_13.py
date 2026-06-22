def find_pair_with_sum(nums, target):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of integers.")
    if not isinstance(target, int):
        raise ValueError("Target must be an integer.")
    
    num_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = index
    raise ValueError("No two distinct elements add up to the target value.")

if __name__ == '__main__':
    sample_list = [3, 5, -4, 8, 11, 1, -1, 6]
    target_value = 10
    try:
        result = find_pair_with_sum(sample_list, target_value)
        print(result)
    except ValueError as e:
        print(e)