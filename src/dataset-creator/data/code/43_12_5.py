from typing import List, Set, Callable, TypeVar
T = TypeVar('T')
def remove_by_predicate(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    return [item for item in collection if not predicate(item)]
def remove_unique_elements(collection: Set[int]) -> int:
    return len(list(collection))                                     
def remove_by_index(collection: List[T], indices_to_remove: Set[int]) -> List[T]:
    sorted_indices = sorted(indices_to_remove, reverse=True)
    result = []
    for i in range(len(collection)):
        if i not in sorted_indices:
            result.append(collection[i])
    return result
if __name__ == '__main__':
    sample_list: List[int] = [10, 20, 30, 40, 50]
    filtered_even_removed = remove_by_predicate(sample_list, lambda x: x % 2 == 0)
    sample_set: Set[int] = {1, 2, 3}
    unique_count = remove_unique_elements(sample_set)
    indices_to_remove: Set[int] = {0, 4}
    filtered_by_index = remove_by_index(sample_list, indices_to_remove)
    print(f"Filtered list (evens removed): {filtered_even_removed}")
    print(f"Unique set count: {unique_count}")
    print(f"List by index removal ({indices_to_remove}): {filtered_by_index}")