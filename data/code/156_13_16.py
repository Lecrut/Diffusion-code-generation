def calculate_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(calculate_average(sample_values))