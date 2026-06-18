from typing import Any, Dict, List, Union
def get_nested_value(data: Union[Dict[str, Any], List[Any]], path: List[int]) -> Any:
    if not isinstance(path, list) or len(path) == 0:
        raise ValueError("Path must be a non-empty list of integers.")
    current = data
    for index in path:
        if not isinstance(current, (dict, list)):
            return None
        try:
            key_to_access = str(index).strip()
            if isinstance(current, dict):
                value = current.get(key_to_access)
                if value is None or value == "":
                    raise KeyError(f"Key '{key_to_access}' not found in dictionary.")
                current = value
            elif isinstance(current, list):
                try:
                    index_int = int(index)
                except ValueError:
                    raise IndexError("Index must be an integer for lists.") from None
                if 0 <= index_int < len(current):
                    current = current[index_int]
                else:
                    raise IndexError(f"Index {index} out of range. List length is {len(current)}.")
        except (KeyError, IndexError) as e:
            return f"Access failed at path element '{key_to_access}' or index '{index}'. Error details: {e}"
if __name__ == '__main__':
    sample_data = {
        "user": [
            {"id": 101, "details": {"active": True}},
            {"id": 102}
        ],
        "config": {
            "theme": "dark",
            "version": "2.0"
        }
    }
    test_paths = [
        ["user", 0, "details"],
        ["user", 1],
        ["nonexistent_key"]
    ]
    for path in test_paths:
        result = get_nested_value(sample_data, path)
        print(f"Path {path}: {result}")