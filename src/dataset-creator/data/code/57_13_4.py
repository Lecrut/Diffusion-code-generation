from typing import Any, Union, List, Tuple
class ElementFetcher:
    def get(self, container: Union[List[Any], Tuple[Any]], index: int) -> Any:
        if not isinstance(container, (list, tuple)):
            raise TypeError("Container must be a list or tuple.")
        if index < 0 or index >= len(container):
            raise IndexError(f"Index {index} is out of range for length {len(container)}.")
        return container[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    fetcher = ElementFetcher()
    print(fetcher.get(sample_list, 2))                  
    print(fetcher.get(sample_tuple, 1))                
    try:
        print(fetcher.get(sample_list, -5))
    except IndexError as e:
        print(f"Error caught: {e}")