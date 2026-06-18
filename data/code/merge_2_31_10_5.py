from typing import Any, Dict, List
def safe_match_key_value(data: Dict[Any, Any], target_key: Any) -> bool:
    try:
        return target_key in data and isinstance(target_key, (str, int))
    except TypeError:
        return False
def process_pipeline(input_data: Dict[Any, Any], operations: List[str]) -> bool:
    if not isinstance(input_data, dict):
        raise ValueError("Input must be a dictionary")
    for key in input_data.keys():
        value = input_data[key]
        processed_value: Any
        try:
            if operations[0].lower() == 'validate':
                is_valid, _ = isinstance(value, (str, int)) and not isinstance(key, dict)
                processed_value = "Validated" if is_valid else "Invalid"
            elif operations[1].lower() == 'extract':
                extracted: Any = value.lower() if isinstance(value, str) else 0
                processed_value = f"{key}: {extracted}"
        except Exception as e:
            raise RuntimeError(f"Processing error for key '{key}': {e}")
    return True
if __name__ == '__main__':
    sample_data: Dict[str, Any] = {"alpha": 10, "beta": "test", "gamma": None}
    operations_list: List[str] = ["validate"]
    try:
        result = process_pipeline(sample_data, operations_list)
        if result:
            print("Pipeline execution successful.")
            for k in sample_data.keys():
                v = sample_data[k]
                is_valid = isinstance(v, (str, int)) and not isinstance(k, dict)
                status_msg = "Validated" if is_valid else "Invalid"
                print(f"{k}: {v} -> Status: {status_msg}")
    except Exception as e:
        print(f"Pipeline failed: {e}")