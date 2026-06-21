def filter_duplicates(nums):
    result = []
    i = 0
    while i < len(nums):
        if nums[i] not in result:
            result.append(nums[i])
        i += 1
    return result

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(filter_duplicates(sample_values))