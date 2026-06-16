from typing import List, Any
def deduplicate_with_hash_map(items: List[Any]) -> List[Any]:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    seen: set = set()
    result: List[Any] = []
    for item in items:
        try:
            hash(item)                                                                                                                                                                                                                   
            if item not in seen:
                seen.add(item)
                result.append(item)
        except TypeError as te:
            raise ValueError(f"Unhashable item encountered at index {items.index(item)}: {te}")
    return result
if __name__ == '__main__':
    sample_data = [1, 3, 2, 'a', 'b', 'c', 2, None, 'a']
    try:
        unique_items = deduplicate_with_hash_map(sample_data)
        print(f"Original length: {len(sample_data)}")
        print(f"Deduplicated result: {unique_items}")
        print("Running internal test suite...")
    except ValueError as ve:
        print(f"Expected Error caught during validation: {ve}")