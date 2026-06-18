import json
from typing import Any, Dict, List, Union
def normalize_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, sort_keys=True)
    elif hasattr(value, '__str__'):
        return str(value)
    else:
        raise ValueError(f"Unsupported type for normalization: {type(value)}")
def extract_id(item: Any) -> Union[str, int]:
    if isinstance(item, dict):
        id_key = "id" if "id" in item else list(item.keys())[0]
        return str(item[id_key])
    elif hasattr(item, '__iter__') and not isinstance(item, (str, bytes)):
        try:
            return json.dumps(list(item))[:16].replace(" ", "")
        except Exception:
            return "unknown"
    else:
        return str(id(item))
def process_items(items: List[Any]) -> Dict[str, Any]:
    result = {}
    for item in items:
        try:
            normalized_data = normalize_value(item)
            unique_id = extract_id(item)
            if not isinstance(normalized_data, str):
                continue
            final_key = f"{unique_id}"
            while final_key in result and len(result[final_key]) > 0:
                base_parts = final_key.rsplit(".", maxsplit=1)
                if len(base_parts) == 2:
                    num_part = int(base_parts[-1].replace(" ", "")) + 1
                    new_suffix = f"{num_part}"
                    final_key = f"{base_parts[0]}.{new_suffix}"
            result[final_key] = {
                "original": item,
                "normalized_data": normalized_data,
                "type_info": type(item).__name__
            }
        except Exception as e:
            print(f"Error processing item: {e}")
    return result
if __name__ == '__main__':
    sample_items = [
        {"id": 101, "name": "Alice", "age": 30},
        ["Project Alpha", "Budget $5k"],
        "Meeting Notes: Q4 Review",
        {"project_code": "PRJ-2024"},
    ]
    organized_data = process_items(sample_items)
    print(json.dumps(organized_data, indent=2))