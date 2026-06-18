from typing import TypeVar, Generic, List, Set, Dict, Any, Iterable
T = TypeVar('T')
class CollectionChecker(Generic[T]):
    def __init__(self, collection: Iterable[T]) -> None:
        self.collection = list(collection) if not isinstance(self.collection, (list, set)) else self.collection
    def contains(self, item: T) -> bool:
        return item in self.collection
def check_object_in_collections(target: Any, collections: List[Iterable[Any]]) -> Dict[str, bool]:
    results = {}
    for i, collection in enumerate(collections):
        try:
            checker = CollectionChecker(collection)
            results[f"collection_{i}"] = checker.contains(target)
        except Exception as e:
            results[f"collection_{i}_error"] = str(e)
    return results
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'hello', None]
    sample_set = {45.67, True}
    sample_dict_keys = ['a', 'b']
    target_value = "hello"
    all_collections = [sample_list, sample_set, sample_dict_keys]
    results = check_object_in_collections(target_value, all_collections)
    print(results)