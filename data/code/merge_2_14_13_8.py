from typing import List, Any
def deduplicate_array(arr: List[Any]) -> set:
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    seen = set()
    for item in arr:
        try:
            hash(item)
        except TypeError as e:
            raise TypeError(f"Unhashable type encountered during deduplication: {type(item).__name__}") from e
        if item not in seen:
            seen.add(item)
    return seen
if __name__ == '__main__':
    sample_data = [1, "apple", 3.5, "banana", 2, "cherry", None]
    try:
        unique_items = deduplicate_array(sample_data)
        print("Original list:", sample_data)
        print("Deduplicated set:", sorted(unique_items))
        invalid_input = [1, 2, {"a": "b"}]
    except TypeError as e:
        if isinstance(sample_data, list):
            pass 
        else:
            print(f"Error processing sample data: {e}")