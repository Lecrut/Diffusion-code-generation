from typing import Any, List, Dict
def append_to_collection(collection: list) -> None:
    for item in data_items:
        collection.append(item)
data_items = [
    "string_value",
    {"nested_key": 123},
    [[4, 5], ["six"]],
]
if __name__ == '__main__':
    my_collection: list[Any] = [0, 1]
    append_to_collection(my_collection)
    print(f"Final Collection: {my_collection}")