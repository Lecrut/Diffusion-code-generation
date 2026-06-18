from typing import Any, Sequence
def get_last_element(collection: Sequence[Any]) -> Any:
    if not collection:
        raise IndexError("Collection is empty")
    return collection[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 'a', None]
    result = get_last_element(sample_list)
    print(result)