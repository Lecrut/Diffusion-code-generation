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
            raise TypeError(f"Unhashable type encountered: {type(item).__name__}") from e
    return result
if __name__ == '__main__':
    sample_input = [1, 2, 3, 4, 5] + list(range(6, 9)) * 2
    output = deduplicate_array(sample_input)
    print(output)