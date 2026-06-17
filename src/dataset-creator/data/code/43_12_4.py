from typing import List, Iterator, Any
def remove_items(collection: List[Any], items_to_remove: Any) -> List[Any]:
    return [item for item in collection if item not in items_to_remove]
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    result: List[str] = remove_items(sample_list, 'banana')
    print(result)