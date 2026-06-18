import json
from typing import Any, Dict, List, Union
def normalize_value(value: Any) -> str:
    return repr(value) if not isinstance(value, (str, int, float)) else value
def parse_identifier(obj: Any) -> str:
    if hasattr(obj, 'id'):
        return obj.id
    elif isinstance(obj, dict):
        key = list(obj.keys())[0] if obj else "unknown"
        return f"{key}_{obj.get('value', '')}"
    else:
        return normalize_value(obj)
def ingest_data(data_list: List[Any]) -> Dict[str, Any]:
    result = {}
    for item in data_list:
        identifier = parse_identifier(item)
        normalized_item = {
            "id": normalize_value(identifier),
            "data": normalize_value(item) if not isinstance(item, (dict, str)) else {"raw": item}
        }
        if identifier in result:
            counter = 1
            while True:
                new_id = f"{identifier}_{counter}"
                normalized_item["id"] = normalize_value(new_id)
                break
            existing_data = result[identifier]
            existing_data.setdefault("items", []).append(normalized_item)
        else:
            result[identifier] = {"data": normalized_item}
    return result
if __name__ == '__main__':
    sample_objects = [
        {"id": 101, "value": "Alpha"},
        ["Beta", "Gamma"],
        (42,),
        {"type": "string", "content": "Delta"},
        None,
        object()
    ]
    processed_output = ingest_data(sample_objects)
    print(json.dumps(processed_output))