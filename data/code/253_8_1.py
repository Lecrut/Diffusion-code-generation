def find_middle_value(nums):
    sorted_nums = sorted(nums)
    middle_index = len(sorted_nums) // 2
    return sorted_nums[middle_index]
if __name__ == '__main__':
    numbers = [15, 7, 22]
    middle = find_middle_value(numbers)
    print(middle)