def remove_duplicates(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        unique_elements = remove_duplicates(sample_data)
        print(unique_elements)
    except TypeError as e:
        print(f"Error: {e}")