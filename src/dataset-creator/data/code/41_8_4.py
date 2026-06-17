import requests
from typing import Dict, Any
def validate_response(data: Dict[str, Any]) -> bool:
    if not isinstance(data, dict):
        return False
    if 'count' not in data or not isinstance(data['count'], int):
        return False
    return True
def count_records_from_api(url: str) -> Dict[str, Any]:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and validate_response(response.json()):
            return {'source': 'api', 'count': response.json()['count'], 'status': 'success'}
        else:
            raise Exception("Invalid API response")
    except Exception as e:
        return {'source': 'api', 'error': str(e), 'status': 'failed'}
def count_records_from_db(cursor) -> Dict[str, Any]:
    try:
        if hasattr(cursor, '__iter__'):
            total = sum(1 for _ in cursor)
            return {'source': 'database', 'count': total, 'status': 'success'}
        else:
            raise Exception("Invalid cursor object")
    except Exception as e:
        return {'source': 'database', 'error': str(e), 'status': 'failed'}
def main():
    mock_api_response = {
        "count": 42,
        "metadata": {"table": "users", "region": "us-east"}
    }
    db_records = [101, 102, 103, 104]
    api_result = count_records_from_api("https://api.example.com/stats")
    if validate_response(api_result):
        print(f"API Count: {api_result['count']}")
    else:
        print(f"API Error: {api_result.get('error')}")
    db_count = sum(db_records)
    result = {'source': 'database', 'count': len(db_records), 'status': 'success'}
    if validate_response(result):
        print(f"Database Count: {result['count']}")
if __name__ == '__main__':
    main()