def validate_input(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements in the list must be integers.")

def compare_adjacent_ascending(nums):
    validate_input(nums)
    return [nums[i] < nums[i + 1] for i in range(len(nums) - 1)]

if __name__ == '__main__':
    sample_values = [5, 7, 6, 8, 9]
    result = compare_adjacent_ascending(sample_values)
    print(result)