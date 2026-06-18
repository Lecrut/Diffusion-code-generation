from typing import TypeVar, Union, List, Tuple
T = TypeVar('T')
def get_last_element(collection: Union[List[T], Tuple[...]]) -> T:
    if not collection:
        raise ValueError("Collection is empty")
    return collection[-1]
if __name__ == '__main__':
    sample_list: List[int] = [1, 2, 3, 4, 5]
    sample_tuple: Tuple[str, ...] = ("a", "b", "c")
    result_int: int = get_last_element(sample_list)
    result_str: str = get_last_element(sample_tuple)
    print(result_int)
    print(result_str)