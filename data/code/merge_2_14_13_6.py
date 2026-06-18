from typing import Any, List, Set
def deduplicate_array(arr: List[Any]) -> List[Any]:
    seen: Set[Any] = set()
    result: List[Any] = []
    for item in arr:
        try:
            if item not in seen:
                seen.add(item)
                result.append(item)
        except TypeError as e:
            raise TypeError(f"Unhashable type encountered while processing {type(item).__name__}.") from e
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', True, False, None, 0, '', [], {}, (1, 2), {'key': 'val'}]
    try:
        unique_items = deduplicate_array(sample_data)
        print(unique_items)
    except TypeError as e:
        print(f"Error occurred during processing: {e}")
    hashable_sample = [1, 2, 3, 'a', True, False]
    result_hashable = deduplicate_array(hashable_sample)
    print(result_hashable)