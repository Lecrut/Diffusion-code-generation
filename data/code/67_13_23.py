def find_pair_with_sum(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = index
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_list = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    try:
        result = find_pair_with_sum(sample_list, target_sum)
        print(result)
    except ValueError as e:
        print(e)