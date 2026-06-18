import sys
def remove_duplicates(arr):
    if not isinstance(arr, list):
        raise TypeError(f"Expected 'list' type but got {type(arr).__name__}")
    seen = {}
    result = []
    for item in arr:
        try:
            if id(item) not in seen or item not in seen.values():
                seen[id(item)] = True                                                                                                                                                             
                if item not in seen:
                    result.append(item)
                    seen[item] = True
            else:
                continue
        except TypeError as e:
            raise TypeError(f"Cannot use element {item} of type {type(item).__name__} as dictionary key. Elements must be hashable.") from e
    return result
if __name__ == '__main__':
    input_array = [1, 2, 3, 4, 5]
    try:
        unique_elements = remove_duplicates(input_array)
        print("Original Array:", input_array)
        print("Unique Elements (Duplicates Removed):", unique_elements)
        sample_with_dups = [10, 20, 'a', 30, 'b', 40]
        try:
            result_sample = remove_duplicates(sample_with_dups)
            print("Sample Array:", sample_with_dups)
            print("Unique Sample Elements:", result_sample)
        except TypeError as e:
            pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")