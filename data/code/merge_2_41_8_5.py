import requests
from typing import Dict, Any
def validate_response(data: Dict[str, Any]) -> bool:
    required_fields = ["status", "data"]
    return all(field in data for field in required_fields) and isinstance(data["data"], list)
def count_records(response_data: Dict[str, Any], record_field_name: str = None) -> int:
    if not validate_response(response_data):
        raise ValueError("Invalid response format")
    data_list = response_data.get("data", [])
    count = len(data_list)
    if record_field_name:
        filtered_count = sum(1 for item in data_list if isinstance(item, dict))
        return filtered_count
    return count
if __name__ == '__main__':
    mock_response_data = {
        "status": 200,
        "data": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob", "extra_field": True},
            {"id": 3, "name": "Charlie"}
        ]
    }
    db_query_result = [
        ("101", "Product A"),
        ("102", "Product B")
    ]
    api_count = count_records(mock_response_data, record_field_name="name")
    print(f"API Records Count: {api_count}")