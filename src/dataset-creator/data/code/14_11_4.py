import sys
def remove_duplicates(arr):
    if not isinstance(arr, list):
        raise TypeError(f"Expected 'list', got '{type(arr).__name__}'")
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 5, 2, 1, -9, 3, 3]
    try:
        unique_elements = remove_duplicates(sample_data)
        print(f"Input array: {sample_data}")
        print(f"Unique elements (preserving order): {unique_elements}")
    except TypeError as e:
        print(f"Error processing input data: {e}", file=sys.stderr)