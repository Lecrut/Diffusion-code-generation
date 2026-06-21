def find_pair_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], index]
        num_to_index[num] = index
    raise ValueError("No two sum solution")

if __name__ == '__main__':
    nums = [4, 9, 5, 0, 1]
    target = 9
    result = find_pair_sum(nums, target)
    print(result)