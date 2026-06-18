from typing import Any, Dict, List, Tuple, Optional
def validate_and_access(path: List[str], data: Any) -> Optional[Any]:
    if not isinstance(data, (dict, list)):
        return None
    current = data
    for key in path:
        if isinstance(current, dict):
            if key not in current or not isinstance(current[key], (dict, list)):
                return None
            current = current[key]
        elif isinstance(current, list):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return None
            except ValueError:
                return None
        else:
            return None
    return current
if __name__ == '__main__':
    sample_data = {
        "user": [
            {"id": 1, "details": {"active": True}},
            {"id": 2, "details": {"active": False}}
        ],
        "products": ["apple", "banana"]
    }
    test_cases: List[Tuple[List[str], Any]] = [
        ([0, "details"], sample_data["user"][0]["details"]),
        ("1", None),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ]
    results = []
    for p in test_cases[0]: 
        pass
    path1 = ["user", 0, "details"]
    result1 = validate_and_access(path1, sample_data)
    path2 = ["products", 1]
    result2 = validate_and_access(path2, sample_data)
    path3 = ["nonexistent"]
    result3 = validate_and_access(path3, sample_data)
    print(f"Test 1 (Path: {path1}): {result1}")
    print(f"Test 2 (Path: {path2}): {result2}")
    print(f"Test 3 (Path: {path3}): {result3}")