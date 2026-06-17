from typing import Callable, List, TypeVar
T = TypeVar('T')
def filter_elements(collection: List[T], predicate: Callable[[T], bool]) -> List[T]:
    return [item for item in collection if predicate(item)]
def remove_duplicates_preserve_order(sequence: T) -> List[T]:
    seen = set()
    result = []
    def _is_new(x):
        return x not in seen
    for item in sequence:
        if _is_new(item):
            seen.add(item)
            result.append(item)
    return result
def process_collection(data: List[int]) -> int:
    def is_odd(n: int) -> bool:
        return n % 2 == 1
    filtered = filter_elements(data, lambda x: is_odd(x))
    total = sum(map(lambda item: item * 2, filtered))
    return total
if __name__ == '__main__':
    sample_data = [10, 3, 5, 7, 8, 9]
    result = process_collection(sample_data)
    print(result)