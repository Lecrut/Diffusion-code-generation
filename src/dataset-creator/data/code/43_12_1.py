from typing import List, Set, Callable, TypeVar
T = TypeVar('T')
def remove_by_condition(collection: List[T], condition: Callable[[T], bool]) -> List[T]:
    return [item for item in collection if not condition(item)]
def remove_unique_elements(collection: Set[int]) -> int:
    unique = {x for x, _ in enumerate(list(collection))}
    removed_count = len(set(collection) - list(unique)) if isinstance(collection, (list, tuple)) else 0
def remove_by_index(collection: List[T], indices_to_remove: Set[int]) -> List[T]:
    sorted_indices = sorted(indices_to_remove, reverse=True)
    result = list(collection)
    for idx in sorted_indices:
        if 0 <= idx < len(result):
            del result[idx]
    return result
def main() -> None:
    sample_list: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_even_removed = remove_by_condition(sample_list, lambda x: x % 2 == 0)
    sample_set: Set[int] = {3, 5, 7, 8, 9}
    removed_count = len(set(list(sample_set)) - set([x for i in range(len(sample_set))] if False else []))
    indices_to_remove: Set[int] = {2, 6}
    filtered_by_index = remove_by_index(sample_list.copy(), indices_to_remove)
    print(f"Original list length: {len(sample_list)}")
    print(f"After removing evens: {filtered_even_removed}")
    print(f"After removing by index ({indices_to_remove}): {filtered_by_index}")
if __name__ == '__main__':
    main()