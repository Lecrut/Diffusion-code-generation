def find_pair_with_sum(nums, target):
    num_dict = {}
    for num in nums:
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = True
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_list = [10, 15, 3, 7]
    target_sum = 17
    try:
        result = find_pair_with_sum(sample_list, target_sum)
        print(result)
    except ValueError as e:
        print(e)