def find_pair_sum(nums, target):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("nums must be a list of integers")
    if not isinstance(target, int):
        raise ValueError("target must be an integer")

    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

    raise ValueError("No two sum solution")

if __name__ == '__main__':
    nums = [1, 5, 7, 3]
    target = 8
    result = find_pair_sum(nums, target)
    print(result)