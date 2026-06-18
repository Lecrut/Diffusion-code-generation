from typing import Any, List, Set
def deduplicate_items(items: List[Any]) -> List[Any]:
    seen: Set[Any] = set()
    result: List[Any] = []
    for item in items:
        if not isinstance(item, (int, float, str, tuple)):
            raise TypeError(f"Unhashable type '{type(item).__name__}' encountered.")
        try:
            seen.add(item)
            result.append(item)
        except TypeError as e:
            raise TypeError(f"Item {item} is unhashable and cannot be used for deduplication.") from e
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(deduplicate_items(sample_data))