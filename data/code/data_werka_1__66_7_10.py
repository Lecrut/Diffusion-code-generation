def compare_adjacent_ascending(nums):
    return [nums[i] < nums[i + 1] for i in range(len(nums) - 1)]

if __name__ == '__main__':
    sample_values = [1, 3, 2, 4, 5]
    result = compare_adjacent_ascending(sample_values)
    print(result)