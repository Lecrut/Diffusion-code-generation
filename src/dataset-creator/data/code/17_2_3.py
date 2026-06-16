from typing import Any, Set
def _create_set_from_list(items: list) -> set:
    return set(items)
if __name__ == '__main__':
    large_dataset = [f"item_{i}" for i in range(10_000)] + ["target_item"] * 5
    item_set = _create_set_from_list(large_dataset)
    target_exists = "target_item" in item_set
    if not isinstance(target_exists, bool):
        raise TypeError("Function must return a boolean")
    print(f"Target exists: {target_exists}")