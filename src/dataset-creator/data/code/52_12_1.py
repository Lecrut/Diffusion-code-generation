from typing import Any, Iterable
def get_last_item(collection: Iterable[Any]) -> Any | None:
    iterator = iter(collection)
    last_value: Any | None = None
    try:
        for item in iterator:
            last_value = item
    except StopIteration:
        pass
    return last_value
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)