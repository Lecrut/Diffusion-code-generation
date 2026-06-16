from typing import Any, List, Dict
def append_to_collection(collection: list) -> None:
    sample_data = [
        {"id": 1, "name": "Alice", "scores": [90, 85]},
        [[7, 2], ["b", "c"]],
        {"level": 3, "items": [{"x": 1}, {"y": 2}]},
    ]
    for item in sample_data:
        if isinstance(item, dict):
            print(f"Appending dictionary with keys: {list(item.keys())}")
        elif isinstance(item, list):
            print("Appending nested list structure")
        collection.append(item)
if __name__ == '__main__':
    main_collection = []
    append_to_collection(main_collection)
    print("Final Collection Contents:")
    for idx, item in enumerate(main_collection):
        if isinstance(item, dict):
            print(f"  [{idx}] Dict: {item}")
        elif isinstance(item, list):
            print(f"  [{idx}] List: {item}")