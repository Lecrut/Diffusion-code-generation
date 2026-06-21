from typing import List, TypeVar, Dict, Any

T = TypeVar('T')

INDEX_OFFSET: int = 1
EMPTY_LIST_ERROR: str = "List cannot be empty"

def get_last_item(data: List[T]) -> T:
    length = len(data)
    if length == 0:
        raise ValueError(EMPTY_LIST_ERROR)
    target_index = length - INDEX_OFFSET
    return data[target_index]

def build_test_registry() -> Dict[str, List[int]]:
    return {
        "integers": [100, 200, 300, 400],
        "floats": [1.5, 2.5, 3.5],
        "mixed": [5, 10, 15]
    }

if __name__ == '__main__':
    registry = build_test_registry()
    for category, values in registry.items():
        last_val = get_last_item(values)
        print(f"{category}: {last_val}")