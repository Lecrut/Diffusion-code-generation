import sys
def remove_duplicates(arr):
    if not isinstance(arr, list):
        raise TypeError(f"Expected 'list' type but received '{type(arr).__name__}'.")
    seen = set()
    result = []
    for item in arr:
        try:
            hash(item)                                    
        except TypeError:
            raise ValueError("All elements must be hashable (e.g., int, str).") from None
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    input_data = [10, 20, 30, 40, 50, 20, 60, 70, 80, 90, 10]
    try:
        unique_elements = remove_duplicates(input_data)
        print(" ".join(map(str, unique_elements)))
    except (TypeError, ValueError) as e:
        print(f"Error processing input: {e}", file=sys.stderr)