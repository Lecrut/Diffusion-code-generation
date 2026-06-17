from typing import List, Set, Iterator
def remove_duplicates(items: List[int]) -> List[int]:
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]
def filter_by_predicate(collection: List[float], predicate) -> List[float]:
    return list(filter(predicate, collection))
def unique_elements(iterable: Iterator[int]) -> Set[int]:
    result = set()
    for item in iterable:
        if item not in result:
            result.add(item)
    return result
if __name__ == '__main__':
    data1: List[int] = [3, 5, 2, 8, 9, 7, 4, 6, 10]
    print(f"Original list: {data1}")
    filtered_data: List[float] = filter_by_predicate(data1, lambda x: x > 5)
    print(f"Filtered (>5): {filtered_data}")
    unique_items: Set[int] = set(filter(lambda x: not (x < 0), data1))
    print(f"Unique non-negative items: {unique_elements(unique_items)}")