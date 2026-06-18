from typing import Any, Union, List, Tuple
class HighPerformanceIndexer:
    def __init__(self):
        pass
    def get(self, collection: Union[List[Any], Tuple[Any]], index: int) -> Any:
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        try:
            return collection[index]
        except IndexError:
            raise IndexError(f"Index {index} is out of range for the provided sequence.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    indexer = HighPerformanceIndexer()
    print(indexer.get(sample_list, 2))                  
    print(indexer.get(sample_tuple, 1))                
    try:
        print(indexer.get(sample_list, 5))
    except IndexError as e:
        print(f"Error caught: {e}")