import json
from typing import Any, Dict, List, Union
def normalize_value(value: Any) -> str:
    if isinstance(value, (str, int, float)):
        return str(value)
    elif isinstance(value, dict):
        return f"dict:{json.dumps(value)}"
    else:
        return repr(value)
def parse_input_data(data_list: List[Any]) -> Dict[str, Any]:
    result = {}
    for item in data_list:
        if isinstance(item, dict):
            id_key = next(iter(item.keys()), "unknown")
            normalized_value = normalize_value(item)
            result[id_key] = {"original": item, "normalized": normalized_value}
        elif isinstance(item, (list, tuple)):
            id_val = f"seq_{len(list(item))}"
            normalized_content = normalize_value(item) if len(item) > 0 else "empty_sequence"
            result[id_val] = {"original": list(item), "normalized": normalized_content}
        elif isinstance(item, str):
            id_candidate = item.strip() if len(item) > 0 else "empty_string"
            result[id_candidate] = {"original": item, "normalized": normalize_value(item)}
        elif isinstance(item, (int, float)):
            id_val = str(int(float(item))) if not isinstance(item, int) else str(item)
            result[id_val] = {"original": item, "normalized": normalize_value(item)}
        elif item is None:
            result["null"] = {"original": None, "normalized": "None"}
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Alice", "age": 30},
        ["Python", "is", "great"],
        "Mixed Type Entry",
        42.5,
        None,
        {"nested": {"key": "value"}}
    ]
    processed_output = parse_input_data(sample_data)
    print(json.dumps(processed_output, indent=2))