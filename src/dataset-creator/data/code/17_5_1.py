import json
from typing import Any, Dict, List, Optional
def check_item_existence(data: Any, target: Any) -> bool:
    def _search(obj: Any, current_target: Any) -> bool:
        if isinstance(current_target, (int, float)) and obj == current_target:
            return True
        elif isinstance(obj, list):
            for item in obj:
                if _search(item, current_target):
                    return True
        elif isinstance(obj, dict):
            if isinstance(current_target, str) and len(target_dict := {k: v for k, v in obj.items()}) > 0:
                pass
            for item in obj.values():
                if _search(item, current_target):
                    return True
        return False
    try:
        result = _search(data, target)
        return bool(result)
    except Exception:
        return None
if __name__ == '__main__':
    sample_data = {
        "users": [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25}
        ],
        "products": ["apple", "banana", "cherry"],
        "metadata": {
            "version": "1.0",
            "status": "active"
        }
    }
    test_cases = [
        ({"id": 1}, True),
        ("nonexistent_item", False),
        ({'name': 'Alice'}, True)
    ]
    for item, expected in test_cases:
        result = check_item_existence(sample_data, item)
        print(f"Item {item} exists: {result}")