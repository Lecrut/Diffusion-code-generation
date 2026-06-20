def is_sorted_ascending(nums):
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements must be integers")
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(is_sorted_ascending(sample_values))