from typing import Any, List, Tuple, Union
def get_last_element(collection: List[Any] | Tuple[Any, ...]) -> Any:
    return collection[-1] if collection else None
if __name__ == '__main__':
    data_list = [10, 20, 'hello', True]
    data_tuple = (3.14, False, "end")
    result_list: Any = get_last_element(data_list)
    result_tuple: Any = get_last_element(data_tuple)
    print(f"List last element: {result_list}")
    print(f"Tuple last element: {result_tuple}")