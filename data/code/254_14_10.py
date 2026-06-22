def flatten_and_find_min(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_min(item))
        else:
            flat_list.append(item)
    return min(flat_list)

if __name__ == '__main__':
    sample1 = [3, 5, [2, 1], 4]
    sample2 = [[-1, -3, [-2]], 0]
    print(f"Minimum in {sample1}: {flatten_and_find_min(sample1)}")
    print(f"Minimum in {sample2}: {flatten_and_find_min(sample2)}")