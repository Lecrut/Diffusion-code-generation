def find_pair_with_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = index
    raise ValueError("No pair found that adds up to the target value.")

if __name__ == '__main__':
    sample_list = [3, 1, 5, 7]
    target_value = 8
    try:
        result = find_pair_with_sum(sample_list, target_value)
        print(result)
    except ValueError as e:
        print(e)