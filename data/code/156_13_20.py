def calculate_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    print(calculate_average(sample_values))