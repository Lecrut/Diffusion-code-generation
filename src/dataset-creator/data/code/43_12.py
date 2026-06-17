from typing import List, Set, Callable, TypeVar
T = TypeVar('T')
def remove_by_predicate(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    return [item for item in collection if not predicate(item)]
def remove_unique_elements(collection: Set[T], unique_value: T) -> Set[T]:
    new_set = {x for x in collection if x != unique_value}
    return new_set
if __name__ == '__main__':
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    items_to_remove_by_condition: Callable[[int], bool] = lambda x: x % 2 == 0
    filtered_numbers: List[int] = remove_by_predicate(numbers, items_to_remove_by_condition)
    sample_set: Set[str] = {'apple', 'banana', 'cherry'}
    value_to_delete: str = 'banana'
    cleaned_set: Set[str] = remove_unique_elements(sample_set, value_to_delete)
    print(f"Filtered numbers (odds only): {filtered_numbers}")
    print(f"Cleaned set without banana: {cleaned_set}")