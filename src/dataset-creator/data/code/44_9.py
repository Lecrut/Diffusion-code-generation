from typing import Any, Dict, List, Tuple
def get_nested_value(data: Dict[str, Any], path: List[Any]) -> Any:
    current = data
    for key in path:
        if isinstance(current, dict):
            if not isinstance(key, str) or key not in current:
                return None
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return None
            except (ValueError, TypeError):
                return None
        else:
            return None
    return current
if __name__ == '__main__':
    sample_data = {
        "user": {
            "profile": {
                "age": 30,
                "hobbies": ["reading", "coding"]
            },
            "address": {"city": "New York"}
        }
    }
    test_paths = [
        ("user", "profile", "age"),
        (["user"], ["profile"]),
        ([1], 0),
        ("nonexistent_key", []),
        ("user", "missing_section")
    ]
    for path in test_paths:
        result = get_nested_value(sample_data, list(path)) if isinstance(path[0], str) else get_nested_value(sample_data, [path])
        print(f"Path {list(path)} -> Value: {result}")