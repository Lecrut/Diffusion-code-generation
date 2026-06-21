def find_pair_sum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    raise ValueError("No two sum solution")

if __name__ == '__main__':
    nums = [4, 9, 11, 3, 7]
    target = 14
    result = find_pair_sum(nums, target)
    print(result)