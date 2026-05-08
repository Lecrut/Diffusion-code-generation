def reverse_two_numbers(nums):
    return [nums[1], nums[0]]
if __name__ == '__main__':
    sample_list = [10, 20]
    reversed_list = reverse_two_numbers(sample_list)
    print(reversed_list)