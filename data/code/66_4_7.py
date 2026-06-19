def is_strictly_increasing(nums):
    result = []
    for i in range(len(nums) - 1):
        result.append(nums[i] < nums[i + 1])
    return result

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 3.1, 4.8, 5.0]
    print(is_strictly_increasing(sample_values))