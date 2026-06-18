def remove_duplicates(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    seen = set()
    result = []
    for item in arr:
        try:
            hash(item)                                
        except TypeError:
            raise ValueError(f"Element {item} is not hashable and cannot be processed.") from None
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        unique_elements = remove_duplicates(sample_data)
        print(f"Original array: {sample_data}")
        print(f"Deduplicated array: {unique_elements}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")