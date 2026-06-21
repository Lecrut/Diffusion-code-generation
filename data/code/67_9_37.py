MAX_LIST_SIZE = 10**4
NUM_TYPE = int

def find_pair_sum(nums, target):
    if not isinstance(nums, list) or len(nums) > MAX_LIST_SIZE:
        raise ValueError("nums must be a list with size up to {}".format(MAX_LIST_SIZE))
    if not all(isinstance(x, NUM_TYPE) for x in nums):
        raise ValueError("All elements in nums must be integers")
    if not isinstance(target, NUM_TYPE):
        raise ValueError("target must be an integer")
    
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError("No two sum solution")

if __name__ == '__main__':
    nums = [10, 15, 3, 7]
    target = 17
    result = find_pair_sum(nums, target)
    print(result)