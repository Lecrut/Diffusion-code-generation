import requests
from typing import Dict, Any
def validate_response(data: Dict[str, Any]) -> bool:
    required_fields = ["status", "data"]
    return all(field in data for field in required_fields) and isinstance(data["data"], list)
def count_records(response_data: Dict[str, Any], validation_required: bool = True) -> int:
    if not validate_response(response_data):
        raise ValueError("Invalid response structure")
    return len(response_data["data"])
if __name__ == '__main__':
    sample_db_result = {
        "status": 200,
        "data": [1, 2, 3, 4, 5]
    }
    api_response_mock = {
        "status": 201,
        "data": ["item_a", "item_b"]
    }
    db_count = count_records(sample_db_result)
    print(f"Database records: {db_count}")
    if validate_response(api_response_mock):
        api_count = len(api_response_mock["data"])
        print(f"API records: {api_count}")
    else:
        print("Failed to process API response")