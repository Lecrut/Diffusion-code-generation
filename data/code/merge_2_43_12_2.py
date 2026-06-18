from typing import List, Set, Callable, TypeVar
T = TypeVar('T')
def remove_by_condition(collection: List[T], condition: Callable[[T], bool]) -> List[T]:
    return [item for item in collection if not condition(item)]
def remove_unique_elements(collection: Set[int], unique_value: int) -> Set[int]:
    new_set = {x for x in collection if x != unique_value}
    return new_set
def filter_and_transform(items: List[str]) -> List[str]:
    return [item.upper() for item in items if 'a' in item.lower()]
if __name__ == '__main__':
    sample_list = [3, 5, 7, 9, 11]
    filtered_numbers = remove_by_condition(sample_list, lambda x: x % 2 != 0)
    unique_set = {1, 2, 3}
    cleaned_unique = remove_unique_elements(unique_set, 2)
    text_items = ["apple", "banana", "cherry"]
    transformed_text = filter_and_transform(text_items)
    print(f"Filtered numbers: {filtered_numbers}")
    print(f"Cleaned unique set: {cleaned_unique}")
    print(f"Transformed text: {transformed_text}")