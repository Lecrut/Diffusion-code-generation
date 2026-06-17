from typing import Any, List, Tuple, Union
class ElementFetcher:
    def __init__(self):
        pass
    @staticmethod
    def fetch(data: Union[List[Any], Tuple[Any, ...]], index: int) -> Any:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        length = len(data)
        if index < -length or index >= length:
            raise IndexError(f"Index {index} is out of range for sequence with length {length}")
        return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    result_from_list = ElementFetcher.fetch(sample_list, -1)
    print(f"List element at last index: {result_from_list}")
    result_from_tuple = ElementFetcher.fetch(sample_tuple, 2)
    print(f"Tuple element at middle index: {result_from_tuple}")