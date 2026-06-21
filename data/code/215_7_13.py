def flatten_and_find_max(nested_list):
    flattened = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened.extend(flatten_and_find_max(sublist))
        else:
            flattened.append(sublist)
    return max(flattened)

if __name__ == '__main__':
    sample_list = [[1, 5], [3, 2], [9, 4]]
    print(f"Largest in {sample_list}: {flatten_and_find_max(sample_list)}")