def filter_duplicates(nums):
    result = []
    seen = set()
    i = 0
    while i < len(nums):
        if nums[i] not in seen:
            result.append(nums[i])
            seen.add(nums[i])
        i += 1
    return result

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(filter_duplicates(sample_values))