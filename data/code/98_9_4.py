def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'result' in data:
            if data['result'] == 'success':
                return {"status": "success", "message": "Operation successful", "data": data['result']}
            else:
                return {"status": "error", "message": "API returned success status but internal result failed", "details": data.get('error_detail', 'Unknown internal error')}
        else:
            return {"status": "error", "message": "Invalid data format received", "details": "Missing 'result' field or data is not a dictionary"}
    elif status_code == 400:
        if 'error_code' in data and data['error_code'] == 'INVALID_INPUT':
            return {"status": "error", "message": "Client input validation failed", "details": data.get('error_message', 'Input validation failed')}
        else:
            return {"status": "error", "message": "Client input validation failed", "details": data.get('error_message', 'Unknown validation error')}
    elif status_code == 500:
        if 'error_type' in data and data['error_type'] == 'SERVER_FAILURE':
            return {"status": "error", "message": "Internal Server Error", "details": "The server encountered an unexpected error"}
        else:
            return {"status": "error", "message": "Internal Server Error", "details": "A generic server error occurred"}
    else:
        return {"status": "error", "message": f"Unexpected HTTP Status Code: {status_code}", "details": "No specific error details provided"}
if __name__ == '__main__':
    test_cases = [
        (200, {"result": "success", "data": {"id": 123, "value": 456}}),
        (200, {"result": "failure", "error_detail": "Value out of range"}),
        (200, {"data": "not_a_dict"}),
        (400, {"error_code": "INVALID_INPUT", "error_message": "Field 'name' cannot be empty"}),
        (400, {"error_code": "VALIDATION_ERROR", "error_message": "Missing required field: email"}),
        (500, {"error_type": "SERVER_FAILURE"}),
        (500, {"error_type": "DB_CONNECTION_LOST"}),
        (500, {"error_type": "UNKNOWN_ERROR"}),
        (404, {"error_code": "NOT_FOUND", "error_message": "Resource not found"}),
        (200, None),
    ]
    for status, data in test_cases:
        result = simulate_api_response(status, data)
        print(f"--- Testing Status: {status} ---")
        import json
        print(json.dumps(result, indent=2))
        print("-" * 30)