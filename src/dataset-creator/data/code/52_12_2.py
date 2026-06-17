from typing import Any, Iterable
def get_last_item(collection: Iterable[Any]) -> Any | None:
    try:
        return next(reversed(list(collection)))
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    print(get_last_item(sample_list))
    empty_tuple = ()
    print(get_last_item(empty_tuple))