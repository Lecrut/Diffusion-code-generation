def find_pair_with_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = i
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 9]
    target_sum = 8
    try:
        result = find_pair_with_sum(sample_list, target_sum)
        print(result)
    except ValueError as e:
        print(e)