import json
from typing import Any, Dict, List, Union
def normalize_value(value: Any) -> str:
    return repr(value)
def parse_input_data(data_list: List[Any]) -> Dict[str, Any]:
    result = {}
    for item in data_list:
        if isinstance(item, dict):
            identifier = item.get('id')
            if not identifier:
                identifier = f"auto_{len(result)}"
            result[identifier] = normalize_value(item)
        elif isinstance(item, (list, tuple)):
            normalized_str = str(list(item))
            key = len(result)                                                           
            result[str(key)] = normalized_str
        else:
            item_repr = normalize_value(item)
            if not isinstance(item_repr, str):
                continue                                                             
            existing_keys = [k for k in result.keys() if result[k] == item_repr]
            if len(existing_keys) > 0:
                new_key = f"{existing_keys[0]}_{len(result)}"
            else:
                new_key = str(len(result))
            result[new_key] = item_repr
    return result
if __name__ == '__main__':
    sample_data = [
        {"id": "user_1", "name": "Alice"},
        {"id": "user_2", "age": 30},
        ["item_a", "item_b"],
        (4, 5),
        "plain_string_value",
        None,
    ]
    processed_output = parse_input_data(sample_data)
    print(json.dumps(processed_output))