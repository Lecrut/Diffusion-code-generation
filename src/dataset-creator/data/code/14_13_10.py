from typing import Any, List, Set
def deduplicate_array(arr: List[Any]) -> List[Any]:
    if arr is None or not isinstance(arr, list):
        raise TypeError("Input must be a non-null list.")
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
    sample_input = [1, 2, 3, 'a', 'b', 'c', 4, 5]
    test_case_1: List[Any] = [10, 20, 30, 10, 20, 30, 40]
    try:
        invalid_input = [[1], {'key': 'val'}, (1, 2), [1]]
        deduplicate_array(invalid_input)
    except TypeError as e:
        print(f"Caught expected error for unhashable items: {e}")
    output_1 = deduplicate_array(sample_input)
    output_2 = deduplicate_array(test_case_1)
    print("Sample Output:", output_1)
    print("Test Case 1 Output:", output_2)