from typing import Any, Sequence
def get_last_item(collection: Sequence[Any]) -> Any | None:
    if not collection:
        return None
    return collection[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)
    empty_collection: list[int] = []
    last_empty = get_last_item(empty_collection)
    print(last_empty is None)