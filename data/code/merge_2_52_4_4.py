from typing import Any, List, Tuple
def get_last_element(collection: List[Any] | Tuple[Any, ...]) -> Any:
    return collection[-1] if collection else None
if __name__ == '__main__':
    sample_list = [10, "text", 3.5]
    sample_tuple = (True, {"key": "value"})
    result_list: Any = get_last_element(sample_list)
    result_tuple: Any = get_last_element(sample_tuple)
    print(f"List last element: {result_list}")
    print(f"Tuple last element: {result_tuple}")