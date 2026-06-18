import json
from typing import Any, Dict, List, Union
def normalize_value(value: Any) -> str:
    return str(value).strip() if isinstance(value, (str, int, float)) else repr(value)
def parse_input_data(data_list: List[Any]) -> Dict[str, Any]:
    result = {}
    for item in data_list:
        identifier_key = None
        if isinstance(item, dict):
            first_key = list(item.keys())[0] if item else "unknown"
            identifier_key = normalize_value(first_key)
            normalized_item = {k: v for k, v in item.items() if k != first_key}
        elif isinstance(item, (list, tuple)):
            id_val = str(item[-1]) if len(item) > 0 else "unknown"
            normalized_item = {i: item[i] for i in range(len(item))}
        elif isinstance(item, (str, int, float)):
            identifier_key = normalize_value(str(item) if not isinstance(item, str) else item[:5])
            normalized_item = {"value": item}
        else:
            continue
        final_id = f"{identifier_key}_{id}"
        result[final_id] = {
            "original_type": type(item).__name__,
            "normalized_content": normalize_value(normalized_item) if isinstance(normalized_item, dict) else normalized_item
        }
    return result
if __name__ == '__main__':
    sample_data: List[Any] = [
        {"id": 101, "task": "Review contract", "status": "pending"},
        ["Meeting at 9am", "Location A"],
        "Urgent call with client X",
        {"project_code": "PROJ-204", "deadline": "Nov 30th"}
    ]
    processed_output: Dict[str, Any] = parse_input_data(sample_data)
    print(json.dumps(processed_output, indent=2))