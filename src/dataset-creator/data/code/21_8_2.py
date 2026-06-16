from typing import Any, List, Dict
def append_to_collection(collection: list) -> None:
    samples = [
        {"key": "value", "nested": [1, 2]},
        [[4], ["5"]],
        {6: "seven"},
        [[[8]]]
    ]
    for item in samples:
        collection.append(item)
if __name__ == '__main__':
    main_list = []
    append_to_collection(main_list)
    print(f"Final collection: {main_list}")