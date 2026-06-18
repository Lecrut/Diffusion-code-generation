from typing import Any, Iterable
def get_last_item(collection: Iterable[Any]) -> Any | None:
    try:
        return next(reversed(list(collection)))
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_last_item(sample_list)
    print(result)