def remove_duplicates(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    seen = {}
    result = []
    for item in arr:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result
if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 8, 8]
    try:
        unique_elements = remove_duplicates(sample_array)
        print(unique_elements)
    except TypeError as e:
        print(f"Error: {e}")