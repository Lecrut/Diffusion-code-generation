def compare_adjacent_ascending(nums):
    return [nums[i] < nums[i + 1] for i in range(len(nums) - 1)]

if __name__ == '__main__':
    sample_values = [3, 5, 2, 8, 6]
    result = compare_adjacent_ascending(sample_values)
    print(result)