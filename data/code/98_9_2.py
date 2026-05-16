def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'result' in data:
            if data['result'] == 'success':
                return {"status": "success", "message": "Operation successful", "data": data['result']}
            else:
                return {"status": "error", "message": "API returned success status but internal result failed"}
        else:
            return {"status": "error", "message": "Invalid data format received"}
    elif status_code == 400:
        if 'error_code' in data:
            return {"status": "error", "code": data['error_code'], "message": data.get('error_message', 'Bad Request')}
        else:
            return {"status": "error", "code": 400, "message": "Bad Request, no specific error details"}
    elif status_code == 500:
        if 'details' in data:
            return {"status": "error", "code": 500, "message": "Internal Server Error", "details": data['details']}
        else:
            return {"status": "error", "code": 500, "message": "Internal Server Error, details unavailable"}
    else:
        return {"status": "error", "code": status_code, "message": f"Unknown error status code: {status_code}"}
if __name__ == '__main__':
    response1 = simulate_api_response(200, {"result": "success", "value": 100})
    print("--- Test Case 1 (Success) ---")
    print(response1)
    response2 = simulate_api_response(200, {"result": "failure", "reason": "invalid_input"})
    print("\n--- Test Case 2 (Success Status, Internal Failure) ---")
    print(response2)
    response3 = simulate_api_response(200, {"other_field": "data"})
    print("\n--- Test Case 3 (Success Status, Invalid Data Format) ---")
    print(response3)
    response4 = simulate_api_response(400, {"error_code": 101, "error_message": "Missing required field"})
    print("\n--- Test Case 4 (Client Error 400) ---")
    print(response4)
    response5 = simulate_api_response(400, {"some_other_field": "oops"})
    print("\n--- Test Case 5 (Client Error 400, Missing Details) ---")
    print(response5)
    response6 = simulate_api_response(500, {"details": "Database connection lost"})
    print("\n--- Test Case 6 (Server Error 500, With Details) ---")
    print(response6)
    response7 = simulate_api_response(500, {"some_other_field": "oops"})
    print("\n--- Test Case 7 (Server Error 500, Missing Details) ---")
    print(response7)
    response8 = simulate_api_response(404, {})
    print("\n--- Test Case 8 (Unknown Status Code 404) ---")
    print(response8)