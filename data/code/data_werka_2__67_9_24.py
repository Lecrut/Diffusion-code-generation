def find_pair_sum(nums, target):
    def validate_input():
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise ValueError("nums must be a list of integers")
        if not isinstance(target, int):
            raise ValueError("target must be an integer")

    validate_input()
    
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