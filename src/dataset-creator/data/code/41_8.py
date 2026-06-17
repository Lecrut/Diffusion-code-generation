import json
from typing import Any, Dict, List
def validate_data(data: Any) -> bool:
    return isinstance(data, dict) and "records" in data and len(data["records"]) > 0
def count_records(response: Any) -> int:
    try:
        if isinstance(response, str):
            parsed = json.loads(response)
            data = parsed.get("data", {})
        elif isinstance(response, dict):
            data = response
        else:
            raise ValueError(f"Unsupported input type for counting records")
        validate_data(data)
        return len(data["records"]) if "count" not in data else data.get("count", 0)
    except (json.JSONDecodeError, TypeError):
        print("Validation failed: Invalid response format.")
        raise
if __name__ == '__main__':
    api_response_str = '{"data": {"records": [{"id": 1}, {"id": 2}], "count": 5}}'
    db_result_list = [
        {"user_id": 101, "name": "Alice"},
        {"user_id": 102, "name": "Bob"}
    ]
    count_1: int = count_records(api_response_str)
    print(f"API Records Count: {count_1}")
    db_dict_result = {"records": db_result_list}
    count_2: int = count_records(db_dict_result)
    print(f"Database Records Count: {count_2}")