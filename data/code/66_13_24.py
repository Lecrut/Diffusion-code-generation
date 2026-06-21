def find_adjacent_greater_pairs(nums):
    indices = []
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_values = [3, 8, 6, 7, 5, 9, 2]
    result = find_adjacent_greater_pairs(sample_values)
    print(result)