from typing import TypeVar, Iterable, Any, Optional
T = TypeVar('T')
def get_last_item(collection: Iterable[T]) -> Optional[T]:
    try:
        iterator = iter(collection)
        return next(iterator)[-1] if hasattr(next(iterator), '__getitem__') else None
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list: list[int] = [1, 2, 3, 4, 5]
    result: Optional[int] = get_last_item(sample_list)
    print(result if result is not None else "No items found")