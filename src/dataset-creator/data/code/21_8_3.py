from typing import Any, List, Dict
def append_heterogeneous_data(target: list) -> None:
    SAMPLE_VALUES = [10, 20.5, ["nested_list"], {"outer_key": "inner_value"}]
    target.extend(SAMPLE_VALUES)
if __name__ == '__main__':
    initial_collection = []
    append_heterogeneous_data(initial_collection)
    print(f"Final Collection: {initial_collection}")