import sys
from typing import Any, Union, Tuple, List
class HighPerformanceIndexer:
    def __init__(self):
        pass
    def get_element(self, collection: Union[List[Any], Tuple[Any]], index: int) -> Any:
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        try:
            return collection[index]
        except IndexError:
            raise IndexError(f"Index {index} is out of range for the provided collection.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    indexer = HighPerformanceIndexer()
    print(f"Element at index -1 in list: {indexer.get_element(sample_list, -1)}")
    print(f"Element at index 2 in tuple: '{indexer.get_element(sample_tuple, 2)}'")
    try:
        indexer.get_element(sample_list, 6)
    except IndexError as e:
        print(f"Error caught: {e}")