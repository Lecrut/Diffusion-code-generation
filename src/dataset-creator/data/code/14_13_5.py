from typing import Any, List, Set
def deduplicate_array(arr: List[Any]) -> List[Any]:
    if not isinstance(arr, list):
        raise TypeError(f"Expected a list, got {type(arr).__name__}")
    seen: Set[Any] = set()
    result: List[Any] = []
    for item in arr:
        try:
            hash(item)                                  
        except TypeError as e:
            raise TypeError(f"Unhashable type encountered at index {arr.index(item)}") from e
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_input = [1, 2, 'a', 3.5, 'b', 4, 5]
    try:
        unique_elements = deduplicate_array(sample_input)
        print("Original Array:", sample_input)
        print("Deduplicated Array:", unique_elements)
        assert len(unique_elements) == len(set(unique_elements)), "Duplicate elements found in output"
    except TypeError as te:
        print(f"Deduplication failed due to unhashable items: {te}")