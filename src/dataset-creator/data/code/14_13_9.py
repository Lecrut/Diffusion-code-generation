from typing import List, Any
def deduplicate_array(arr: List[Any]) -> set:
    if not isinstance(arr, list):
        raise TypeError(f"Expected 'list', got {type(arr).__name__}")
    try:
        return set(arr)
    except TypeError as e:
        raise TypeError("Cannot deduplicate unhashable items (e.g., lists or dicts). Ensure input contains only hashable types.") from e
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', None, True, 1, False]
    result = deduplicate_array(sample_data)
    print(f"Deduplicated set: {result}")
    try:
        invalid_input = [[1], 2]
        _ = deduplicate_array(invalid_input)
    except TypeError as e:
        print(f"Caught expected error for unhashable items: {e}")
    edge_case_empty = []
    result_edge = deduplicate_array(edge_case_empty)
    print(f"Deduplicated empty list: {result_edge}")