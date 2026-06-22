def validate_input(nums, target):
    if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums):
        raise ValueError("nums must be a list of integers.")
    if not isinstance(target, int):
        raise ValueError("target must be an integer.")

def find_pair_sum(nums, target):
    validate_input(nums, target)
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

if __name__ == '__main__':
    nums = [3, 2, 4, 6]
    target = 8
    result = find_pair_sum(nums, target)
    print(result)