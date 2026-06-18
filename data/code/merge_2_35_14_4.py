from typing import Any, Dict, Optional
def find_element_by_key(data: Dict[Any, Any], target_key: Any) -> Optional[Any]:
    if not isinstance(data, dict):
        raise TypeError("The first argument must be a dictionary.")
    return data.get(target_key)
if __name__ == '__main__':
    sample_data: Dict[str, int] = {
        "alpha": 10,
        "beta": 20,
        "gamma": 30,
        "delta": 40
    }
    target_key: str = "beta"
    result_value = find_element_by_key(sample_data, target_key)
    print(f"Value for key '{target_key}': {result_value}")