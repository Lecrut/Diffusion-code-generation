from typing import Union, List, Tuple, Any
class ElementFetcher:
    def fetch(self, container: Union[List[Any], Tuple[Any]], index: int) -> Any:
        if not isinstance(container, (list, tuple)):
            raise TypeError("Container must be a list or tuple.")
        try:
            return container[index]
        except IndexError as e:
            raise IndexError(f"Index {index} out of range for length {len(container)}") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    fetcher = ElementFetcher()
    print(fetcher.fetch(sample_list, 2))                  
    print(fetcher.fetch(sample_tuple, 1))                
    try:
        _ = fetcher.fetch(sample_list, -5)                            
    except IndexError as e:
        print(f"Error caught: {e}")