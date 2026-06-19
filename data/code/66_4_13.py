def is_strictly_increasing(nums):
    return [nums[i] < nums[i+1] for i in range(len(nums)-1)]

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 3.1, 4.8, 5.0]
    result = is_strictly_increasing(sample_values)
    print(result)