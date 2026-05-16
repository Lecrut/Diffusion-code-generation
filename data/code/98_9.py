def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'result' in data:
            if data['result'] == 'success':
                return {"status": "success", "message": "Data retrieved successfully", "payload": data['result']}
            else:
                return {"status": "error", "message": "API reported an internal failure", "details": data.get('error_details', 'Unknown error')}
        else:
            return {"status": "error", "message": "Invalid data format received", "details": "Missing 'result' key or data is not a dictionary"}
    elif status_code == 400:
        if 'reason' in data:
            return {"status": "client_error", "message": f"Bad Request: {data['reason']}"}
        else:
            return {"status": "client_error", "message": "Bad Request: Unknown reason"}
    elif status_code == 500:
        if 'error_type' in data:
            return {"status": "server_error", "message": f"Server failed: {data['error_type']}", "details": data.get('traceback', 'No traceback provided')}
        else:
            return {"status": "server_error", "message": "Server encountered an unknown error"}
    else:
        return {"status": "unknown_error", "message": f"HTTP Status Code {status_code} received"}
if __name__ == '__main__':
    test_cases = [
        (200, {"result": "success", "data": [1, 2, 3]}),
        (200, {"result": "failure", "error_details": "Invalid input value"}),
        (200, {"data": "not_a_dict"}),
        (400, {"reason": "Missing required field"}),
        (500, {"error_type": "DatabaseConnectionError", "traceback": "Traceback trace..."}),
        (500, {"message": "Generic Server Crash"}),
        (404, {"reason": "Resource Not Found"}),
        (200, None),
    ]
    for status, data in test_cases:
        result = simulate_api_response(status, data)
        print(f"--- Testing Status: {status} ---")
        print(result)
        print("-" * 20)