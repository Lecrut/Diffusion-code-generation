from typing import Any, List, Tuple, Union
def get_last_element(collection: List[Any] | Tuple[int, ...]) -> Any:
    return collection[-1] if len(collection) > 0 else None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'end']
    sample_tuple = (5.5, True, "final")
    print(get_last_element(sample_list))
    print(get_last_element(sample_tuple))