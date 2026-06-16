from typing import List, Set, TypeVar, Any, Union
T = TypeVar('T')
def deduplicate_items(items: List[Any]) -> List[T]:
    if items is None:
        raise ValueError("Input cannot be null.")
    seen: Set[Any] = set()
    result_list: List[T] = []
    for item in items:
        try:
            hash(item)                                                           
        except TypeError as e:
            raise ValueError(f"Unhashable type encountered at index {items.index(item)}: {e}") from e
        if item not in seen:
            seen.add(item)
            result_list.append(item)
    return result_list
if __name__ == '__main__':
    sample_input = [1, 2, 'a', 'b', 3, 2, None, 'c', None]
    try:
        unique_items = deduplicate_items(sample_input)
        print("Original list:", sample_input)
        print("Deduplicated list:", unique_items)
        test_unhashable = [[1, 2], [3, 4]]
        try:
            deduplicate_items(test_unhashable)
        except ValueError as e:
            print(f"Error detected for unhashable input: {e}")
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}")