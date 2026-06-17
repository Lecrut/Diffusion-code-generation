from typing import Any, Sequence
def get_last_item(collection: Sequence[Any]) -> Any:
    if not collection:
        raise IndexError("Collection is empty")
    return collection[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    try:
        last_val = get_last_item(sample_list)
        print(f"Last item: {last_val}")
        empty_collection = []
        get_last_item(empty_collection)
    except IndexError as exc:
        print(f"Error occurred: {exc}")