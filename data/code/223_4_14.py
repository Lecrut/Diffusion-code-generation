def get_highest_value(nums):
    if not nums:
        raise ValueError("The list is empty")
    return max(nums)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    try:
        print(get_highest_value(sample_values))
    except ValueError as e:
        print(e)