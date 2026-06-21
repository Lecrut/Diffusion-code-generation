def calculate_average(nums):
    return sum(nums) / len(nums) if nums else 0

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    print(calculate_average(sample_values))