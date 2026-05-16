def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'result' in data:
            if data['result'] == 'success':
                return {"status": "success", "message": "Operation successful", "data": data['result']}
            else:
                return {"status": "error", "code": 400, "message": "Data validation failed"}
        else:
            return {"status": "error", "code": 404, "message": "Missing result in response"}
    elif status_code == 401:
        return {"status": "error", "code": 401, "message": "Authentication failed"}
    elif status_code == 403:
        return {"status": "error", "code": 403, "message": "Permission denied"}
    elif status_code == 500:
        return {"status": "error", "code": 500, "message": "Internal server error"}
    else:
        return {"status": "error", "code": 500, "message": f"Unknown error code: {status_code}"}
def process_api_call(status_code, response_data):
    if status_code == 200:
        result = simulate_api_response(status_code, response_data)
        if result['status'] == 'success':
            return result
        else:
            return result
    elif status_code in [401, 403]:
        return simulate_api_response(status_code, None)
    elif status_code == 500:
        return simulate_api_response(status_code, None)
    else:
        return {"status": "error", "code": 500, "message": f"Unhandled status code: {status_code}"}
if __name__ == '__main__':
    test_cases = [
        (200, {"result": "success", "data": [1, 2, 3]}),
        (200, {"result": "failure", "data": []}),
        (200, None),
        (401, None),
        (403, {"error": "Access denied"}),
        (500, {"error": "Database connection lost"}),
        (404, None)
    ]
    print("--- Testing Nested Conditional Logic for API Errors ---")
    for status, data in test_cases:
        print(f"\nTesting Status: {status}, Data: {data}")
        result = process_api_call(status, data)
        print(f"Final Result: {result}")