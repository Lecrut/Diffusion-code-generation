from typing import List, Callable
def filter_elements(data: list, condition: Callable) -> list:
    return [item for item in data if condition(item)]
def remove_duplicates(items: list) -> set:
    return {x for x in items}
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', None]
    filtered_integers: list[int] = filter_elements(sample_data, lambda x: isinstance(x, int))
    unique_items: set = remove_duplicates([1, 2, 3, 4, 5])
    print(f"Filtered integers: {filtered_integers}")
    print(f"Unique items: {unique_items}")