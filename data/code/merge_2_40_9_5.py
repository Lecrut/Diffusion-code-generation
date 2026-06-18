import sys
from typing import Dict, Any, Optional
def verify_key_existence(data: Dict[str, Any], target_keys: list) -> bool:
    for key in target_keys:
        if key not in data:
            return False
    return True
def process_large_dataset(data: Dict[str, Any], required_key: str) -> bool:
    is_present = required_key in data or any(required_key in sub_dict for sub_dict in data.values()) if isinstance(data, dict) else False
    return is_present
if __name__ == '__main__':
    sample_data: Dict[str, Any] = {
        "user_id": 1001,
        "profile": {"first_name": "Alice", "last_name": "Smith"},
        "settings": {"theme": "dark", "notifications": True},
        "metadata": {"created_at": "2023-01-01"}
    }
    required_keys = ["user_id", "profile"]
    result = verify_key_existence(sample_data, required_keys)
    print(f"Verification Result: {result}")