def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'result' in data:
            if data['result'] == 'success':
                return {"status": "success", "message": "Operation successful", "data": data['result']}
            else:
                return {"status": "error", "message": "API returned failure status", "details": data.get('error_detail', 'Unknown failure')}
        else:
            return {"status": "error", "message": "Invalid data structure received", "details": "Missing 'result' field"}
    elif status_code == 400:
        if 'error_code' in data:
            return {"status": "error", "message": "Bad Request", "details": f"Code {data['error_code']}: {data.get('error_message', 'No message provided')}"}
        else:
            return {"status": "error", "message": "Bad Request", "details": "No specific error message provided"}
    elif status_code == 401:
        return {"status": "error", "message": "Unauthorized", "details": "Authentication failed"}
    elif status_code == 500:
        return {"status": "error", "message": "Internal Server Error", "details": "Server encountered an unexpected error"}
    else:
        return {"status": "error", "message": "Unknown Error", "details": f"Received status code {status_code}"}
if __name__ == '__main__':
    response1 = simulate_api_response(200, {"result": "success", "value": 100})
    print("--- Test Case 1 (Success) ---")
    print(response1)
    response2 = simulate_api_response(200, {"result": "failure", "error_detail": "Invalid input"})
    print("\n--- Test Case 2 (Success status, internal failure) ---")
    print(response2)
    response3 = simulate_api_response(200, {"other_data": "missing_result"})
    print("\n--- Test Case 3 (Success status, invalid structure) ---")
    print(response3)
    response4 = simulate_api_response(400, {"error_code": 404, "error_message": "Resource not found"})
    print("\n--- Test Case 4 (Client Error 400) ---")
    print(response4)
    response5 = simulate_api_response(401, {"reason": "token expired"})
    print("\n--- Test Case 5 (Client Error 401) ---")
    print(response5)
    response6 = simulate_api_response(500, {"trace": "database connection lost"})
    print("\n--- Test Case 6 (Server Error 500) ---")
    print(response6)
    response7 = simulate_api_response(400, {"error_message": "Missing required field"})
    print("\n--- Test Case 7 (Client Error 400, minimal detail) ---")
    print(response7)