from typing import List, Set, Any
def deduplicate_array(arr: List[Any]) -> List[Any]:
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    seen: Set[Any] = set()
    result: List[Any] = []
    for item in arr:
        try:
            hash(item)                                                           
        except TypeError as e:
            raise TypeError(f"Cannot deduplicate array containing unhashable items. Error details: {e}") from e
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, "apple", 3, "banana", 2, "cherry", None]
    try:
        unique_items = deduplicate_array(sample_data)
        print("Deduplicated list:", unique_items)
    except TypeError as e:
        print(f"Error occurred: {e}")