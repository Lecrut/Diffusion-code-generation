def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'result' in data:
            if data['result'] == 'success':
                return {"status": "success", "message": "Operation successful", "data": data['result']}
            else:
                return {"status": "error", "message": "API returned success status but internal result was invalid"}
        else:
            return {"status": "error", "message": "Missing or invalid data structure"}
    elif status_code == 400:
        if 'error_code' in data:
            return {"status": "error", "code": data['error_code'], "message": data.get('message', 'Bad Request')}
        else:
            return {"status": "error", "code": 400, "message": "Bad Request, no specific error details provided"}
    elif status_code == 500:
        if 'exception_type' in data:
            return {"status": "error", "code": 500, "message": f"Server Error: {data['exception_type']}"}
        else:
            return {"status": "error", "code": 500, "message": "Internal Server Error"}
    else:
        return {"status": "error", "code": status_code, "message": f"Unknown HTTP Status Code: {status_code}"}
if __name__ == '__main__':
    response1 = simulate_api_response(200, {"result": "success", "value": 100})
    print("--- Test Case 1 (Success) ---")
    print(response1)
    response2 = simulate_api_response(200, {"result": "failure", "detail": "Data mismatch"})
    print("\n--- Test Case 2 (Success Status, Internal Failure) ---")
    print(response2)
    response3 = simulate_api_response(200, None)
    print("\n--- Test Case 3 (Missing Data) ---")
    print(response3)
    response4 = simulate_api_response(400, {"error_code": "INVALID_INPUT", "message": "Field 'x' is required"})
    print("\n--- Test Case 4 (Client Error) ---")
    print(response4)
    response5 = simulate_api_response(500, {"exception_type": "DatabaseConnectionError", "trace": "SQL error"})
    print("\n--- Test Case 5 (Server Error) ---")
    print(response5)
    response6 = simulate_api_response(500, {"message": "Generic Server Failure"})
    print("\n--- Test Case 6 (Generic Server Error) ---")
    print(response6)
    response7 = simulate_api_response(404, {"message": "Resource Not Found"})
    print("\n--- Test Case 7 (Unhandled Status Code) ---")
    print(response7)