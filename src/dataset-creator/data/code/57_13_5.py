from typing import Union, List, Tuple, Any
class ElementFetcher:
    def get_element(self, collection: Union[List[Any], Tuple[Any]], index: int) -> Any:
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        try:
            return collection[index]
        except IndexError as e:
            raise IndexError(f"Index {index} out of range for length {len(collection)}") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    fetcher = ElementFetcher()
    print(fetcher.get_element(sample_list, 2))
    print(fetcher.get_element(sample_tuple, -1))