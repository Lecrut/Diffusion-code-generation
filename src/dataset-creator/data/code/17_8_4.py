from typing import TypeVar, Generic, List, Optional
T = TypeVar('T')
class CollectionChecker(Generic[T]):
    def __init__(self, collection: List[T]) -> None:
        self.collection = collection
    def contains(self, item: T) -> bool:
        return item in self.collection
if __name__ == '__main__':
    sample_list: list[int] = [10, 20, 30, 40]
    checker = CollectionChecker(sample_list)
    test_values: tuple[int, int, str] = (50, 20, "hello")
    for value in test_values:
        try:
            result = checker.contains(value) if isinstance(value, int) else False
            print(f"Value {value} exists: {result}")
        except Exception as e:
            print(f"Error checking type or existence: {e}")