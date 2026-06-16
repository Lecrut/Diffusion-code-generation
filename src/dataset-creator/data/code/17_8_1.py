from typing import TypeVar, Generic, List, Set, Dict, Any, Optional
T = TypeVar('T')
class CollectionChecker(Generic[T]):
    def __init__(self, collection: T):
        self.collection = collection
    @staticmethod
    def contains(collection: Any, item: Any) -> bool:
        try:
            if isinstance(item, (list, tuple)):
                return any(isinstance(c, type(item)) and c == item for c in collection)
            elif hasattr(collection, '__contains__'):
                return item in collection
            else:
                raise TypeError("Collection does not support containment check")
        except Exception as e:
            print(f"Error checking existence: {e}")
            return False
def find_element_in_list(items: List[Any], target: Any) -> Optional[Any]:
    for i, item in enumerate(items):
        if isinstance(item, type(target)) and item == target:
            return items[i]
    return None
if __name__ == '__main__':
    sample_list = [10, 20, "apple", {"key": "value"}]
    sample_set = {5, "banana", (3, 4)}
    sample_dict = [{"id": 1}, {"id": 2}]
    checker = CollectionChecker(sample_list)
    print(f"Is 'apple' in list? {checker.contains(sample_list, 'apple')}")
    print(f"Is [10] in list? {checker.contains(sample_list, [10])}")
    print(find_element_in_list(sample_dict, {"id": 2}))