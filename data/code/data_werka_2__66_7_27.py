def check_ascending_adjacent(nums):
    return [a < b for a, b in zip(nums, nums[1:])]

if __name__ == '__main__':
    test_values = [7, 8, 6, 9, 10]
    print(check_ascending_adjacent(test_values))