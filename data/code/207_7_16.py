def flatten_and_find_max(nested_list):
    flattened = [item for sublist in nested_list for item in (flatten_and_find_max(sublist) if isinstance(item, list) else [item])]
    return max(flattened)

if __name__ == '__main__':
    sample1 = [[3, 5], [2], [8, 9]]
    print(f"Max in {sample1}: {flatten_and_find_max(sample1)}")
    sample2 = [[10, [7]], 4]
    print(f"Max in {sample2}: {flatten_and_find_max(sample2)}")
    sample3 = [[[1], 2], [3, [4, 5]]]
    print(f"Max in {sample3}: {flatten_and_find_max(sample3)}")