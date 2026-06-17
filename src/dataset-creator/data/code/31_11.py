import json
from typing import Any, Dict, List
def extract_keys_recursive(data: Any) -> Dict[str, Any]:
    result = {}
    if isinstance(data, dict):
        for key in data.keys():
            value = data[key]
            try:
                extracted_value = extract_keys_recursive(value)
                if isinstance(extracted_value, dict):
                    for k in extracted_value.keys():
                        result[f"{key}.{k}"] = data[key]
                else:
                    if isinstance(extracted_value, dict):
                         for k in extracted_value.keys():
                             result[f"{key}.{k}"] = data[key]
            except Exception:
                continue
    return result
def process_json_file(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        extracted_data = []
        for item in data:
            try:
                keys_dict = extract_keys_recursive(item)
                if keys_dict or (isinstance(item, dict)):
                    extracted_data.append(keys_dict)
            except Exception:
                continue
        return extracted_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON decoding error in file '{file_path}': {e}")
        return []
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "details": {"nested_key": "value", "deeply_nested": {"inner_1": "a"}}},
        {"id": 2, "status": "active"},
        {},                                         
        None,                                                                             
    ]
    sample_json_str = json.dumps(sample_data)
    import io
    class StringIO:
        def __init__(self, content):
            self.content = content
        def read(self):
            return self.content
        def write(self, s):
            pass                             
    mock_file_obj = StringIO(json.dumps(sample_data))
    try:
        with open('/dev/null', 'w') as f:
            json.dump(mock_file_obj.read(), f)
        result_list = process_json_file('/dev/null')
        print("Extracted Keys Result:")
        for item in result_list[:2]:                                                                       
            print(item)
    except Exception:
        pass