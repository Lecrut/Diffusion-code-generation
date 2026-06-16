from typing import Any, List, Set
def deduplicate_array(arr: List[Any]) -> List[Any]:
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    seen: Set[Any] = set()
    result: List[Any] = []
    for item in arr:
        try:
            hash(item)                                  
        except TypeError as e:
            raise TypeError(f"Unhashable type encountered: {type(item).__name__}") from e
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', 'c', 4, 5]
    test_input_1: List[Any] = [10, 20, 30, 10, 20, 30, 40]
    try:
        bad_input = [[1], {'key': 'val'}, {1}]
        deduplicate_array(bad_input)
    except TypeError as e:
        print(f"Caught expected error for unhashable items: {e}")
    output_1 = deduplicate_array(test_input_1)
    print("Output 1:", output_1)
    empty_output = deduplicate_array([])
    print("Empty Output:", empty_output)