def validate_input(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers.")
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")

def find_zero_sum_pairs(nums):
    validate_input(nums)
    seen = set()
    pairs = []
    for num in nums:
        complement = -num
        if complement in seen and (complement, num) not in pairs and (num, complement) not in pairs:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

if __name__ == '__main__':
    sample_values = [7, -7, 3, -3, 5, -5, 0, 2, -2]
    result = find_zero_sum_pairs(sample_values)
    print(result)