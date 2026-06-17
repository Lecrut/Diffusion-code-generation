from typing import Any, List, Tuple
def get_last_element(collection: List[Any] | Tuple[Any, ...]) -> Any:
    if not collection:
        raise ValueError("Collection is empty")
    return collection[-1]
if __name__ == '__main__':
    sample_list = [10, 20, "apple", None]
    sample_tuple = (3.14, True, ("nested",))
    result_list: Any = get_last_element(sample_list)
    result_tuple: Any = get_last_element(sample_tuple)
    print(f"Last element of list: {result_list}")
    print(f"Last element of tuple: {result_tuple}")