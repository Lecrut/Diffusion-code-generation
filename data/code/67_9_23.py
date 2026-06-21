def find_pair_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError("No two sum solution")

if __name__ == '__main__':
    nums = [5, 3, 6, 8, 2]
    target = 10
    result = find_pair_sum(nums, target)
    print(result)