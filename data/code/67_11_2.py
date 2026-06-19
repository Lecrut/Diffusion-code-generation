def find_pair_with_sum(arr, target):
    index_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in index_map:
            return (complement, num)
        index_map[num] = i
    return None

if __name__ == '__main__':
    sample_array = [2, 4, 6, 8, 10]
    target_value = 14
    result = find_pair_with_sum(sample_array, target_value)
    print(result)