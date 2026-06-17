from typing import Any, Sequence
def get_last_element(collection: Sequence[Any]) -> Any:
    return collection[-1] if len(collection) > 0 else None
if __name__ == '__main__':
    sample_list = [10, 'hello', True, 3.14]
    sample_tuple = (50, 'world')
    print(get_last_element(sample_list))
    print(get_last_element(sample_tuple))