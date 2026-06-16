from typing import TypeVar, Generic, Iterable, List
T = TypeVar('T')
class CollectionChecker(Generic[T]):
    def __init__(self, collection: Iterable[T]) -> None:
        self.collection = list(collection)
    def contains(self, item: T) -> bool:
        return item in self.collection
if __name__ == '__main__':
    sample_list: List[int] = [10, 20, 30, 40]
    checker = CollectionChecker(sample_list)
    test_values: list[T] = [5, 30, 'text']
    for value in test_values:
        result = checker.contains(value)
        print(f"Value {value} exists? {result}")