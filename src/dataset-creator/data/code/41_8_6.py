import json
from typing import Any, Dict, List
def validate_response(data: Any) -> bool:
    return isinstance(data, dict) and "records" in data and len(data["records"]) > 0
def count_records_from_db(cursor_info: Dict[str, Any]) -> int:
    cursor = {
        "rows": [1, 2, 3],
        "columns": ["id", "name"],
        "status_code": 200
    }
    if validate_response(cursor):
        return len(cursor["rows"])
    raise ValueError("Invalid database response structure")
def count_records_from_api(response: Dict[str, Any]) -> int:
    api_data = {
        "total": 105,
        "data": [{"id": i} for i in range(10)]
    }
    if validate_response(api_data):
        return api_data["total"] + len(api_data["data"])
    raise ValueError("Invalid API response structure")
def process_query_results(results: List[Dict[str, Any]]) -> int:
    if not isinstance(results, list):
        return 0
    count = 0
    for result in results:
        try:
            record_count = count_records_from_db(result) or count_records_from_api(result)
            count += int(record_count)
        except ValueError as e:
            print(f"Warning: {e}")
    return count
if __name__ == '__main__':
    db_result = {"records": [{"id": 1}, {"id": 2}]}
    api_result = {"total": 5, "data": []}
    sample_queries = [db_result]
    total_count = process_query_results(sample_queries)
    print(f"Total records processed: {total_count}")