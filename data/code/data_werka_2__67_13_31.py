def find_pair_with_sum(nums, target):
    num_map = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in num_map:
            return (complement, number)
        num_map[number] = index
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_numbers = [10, 15, 3, 7]
    target_value = 17
    try:
        result = find_pair_with_sum(sample_numbers, target_value)
        print(result)
    except ValueError as e:
        print(e)