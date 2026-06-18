from typing import Any, List, Dict
def append_to_collection(collection: List[Any], item: Any) -> None:
    if not isinstance(collection, list):
        raise TypeError("Collection must be a list.")
    try:
        collection.append(item)
    except Exception as e:
        raise RuntimeError(f"Failed to append item due to type constraints or internal error.") from e
if __name__ == '__main__':
    initial_data = [10, 20.5, "text"]
    complex_item = [[4, 5], {"a": 1}, ["b", True]]
    print("Initial collection:", initial_data)
    append_to_collection(initial_data, complex_item)
    print("Final collection after appending nested structures:")
    for idx, element in enumerate(initial_data):
        if isinstance(element, list):
            print(f"  Index {idx}: List -> {element}")
        elif isinstance(element, dict):
            print(f"  Index {idx}: Dict -> {element}")
        else:
            print(f"  Index {idx}: Primitive -> {element}")