def validate_input(nums, target):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise TypeError("The first argument must be a list of integers.")
    if not isinstance(target, int):
        raise TypeError("The second argument must be an integer.")

def find_pair_with_sum(nums, target):
    validate_input(nums, target)
    num_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = index
    raise ValueError("No two distinct elements add up to the target value.")

if __name__ == '__main__':
    sample_list = [3, 6, 8, 12]
    target_value = 14
    try:
        result = find_pair_with_sum(sample_list, target_value)
        print(result)
    except ValueError as e:
        print(e)