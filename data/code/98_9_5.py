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
        if 'details' in data:
            return {"status": "error", "code": 500, "message": "Internal Server Error", "details": data['details']}
        else:
            return {"status": "error", "code": 500, "message": "Internal Server Error, details unavailable"}
    else:
        return {"status": "error", "code": status_code, "message": f"Unknown error status: {status_code}"}
if __name__ == '__main__':
    response1 = simulate_api_response(200, {"result": "success", "value": 100})
    print("--- Test Case 1 (Success) ---")
    print(response1)
    response2 = simulate_api_response(200, {"result": "failure", "reason": "data mismatch"})
    print("\n--- Test Case 2 (Success Status, Internal Failure) ---")
    print(response2)
    response3 = simulate_api_response(200, None)
    print("\n--- Test Case 3 (Missing Data) ---")
    print(response3)
    response4 = simulate_api_response(400, {"error_code": "INVALID_INPUT", "message": "Field 'name' is required"})
    print("\n--- Test Case 4 (Client Error 400) ---")
    print(response4)
    response5 = simulate_api_response(500, {"details": "Database connection timed out"})
    print("\n--- Test Case 5 (Server Error 500 with Details) ---")
    print(response5)
    response6 = simulate_api_response(500, {"some_other_info": "No details provided"})
    print("\n--- Test Case 6 (Server Error 500 without Details) ---")
    print(response6)
    response7 = simulate_api_response(404, {"error": "Not Found"})
    print("\n--- Test Case 7 (Unknown Status Code) ---")
    print(response7)