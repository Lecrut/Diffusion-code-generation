def find_difference(nums):
    if not nums:
        raise ValueError("The tuple must contain at least one number.")
    
    return max(nums) - min(nums)

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 7.8, 0.9)
    try:
        result = find_difference(sample_values)
        print(result)
    except ValueError as e:
        print(e)