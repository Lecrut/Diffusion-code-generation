from typing import Any, Dict, List
def safe_match_key_value(data: Dict[Any, Any], target_key: Any) -> bool:
    try:
        return isinstance(target_key, (str, int)) and data.get(target_key) is not None
    except TypeError:
        return False
def process_pipeline(data: Dict[Any, Any]) -> List[Dict[str, str]]:
    results = []
    for k in list(data.keys()):
        if isinstance(k, (str, int)) and data[k] is not None:
            try:
                v_str = str(data[k])
                results.append({"key": str(k), "value": v_str})
            except Exception:
                continue
    return results
if __name__ == '__main__':
    sample_data = {
        101: "Alice",
        202: None,
        "Bob": 303,
        "Charlie": "404"
    }
    processed_results = process_pipeline(sample_data)
    for item in processed_results:
        print(f"{item['key']}: {item['value']}")