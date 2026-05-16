def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None:
            return {"success": True, "result": data}
        else:
            return {"success": False, "error": "Missing data"}
    elif status_code == 400:
        if "invalid_field" in data:
            return {"success": False, "error": "Validation failed: invalid_field"}
        else:
            return {"success": False, "error": "Validation failed: unknown error"}
    elif status_code == 500:
        if "database_error" in data:
            return {"success": False, "error": "Server error: database_error"}
        else:
            return {"success": False, "error": "Server error: unknown issue"}
    else:
        return {"success": False, "error": f"HTTP Error: {status_code}"}
def process_api_call(status, payload):
    response = simulate_api_response(status, payload)
    if response["success"]:
        return {"status": "OK", "data": response["result"]}
    else:
        error_message = response.get("error", "Unknown processing error")
        return {"status": "ERROR", "details": error_message}
if __name__ == '__main__':
    status_1 = 200
    data_1 = {"id": 101, "value": 42}
    result_1 = process_api_call(status_1, data_1)
    print(f"--- Scenario 1 (Success) ---")
    print(result_1)
    status_2 = 400
    data_2 = {"field": "invalid_field", "value": "test"}
    result_2 = process_api_call(status_2, data_2)
    print(f"\n--- Scenario 2 (Validation Error) ---")
    print(result_2)
    status_3 = 500
    data_3 = {"error_type": "database_error", "details": "Connection lost"}
    result_3 = process_api_call(status_3, data_3)
    print(f"\n--- Scenario 3 (Server Error) ---")
    print(result_3)
    status_4 = 500
    data_4 = {"error_type": "timeout"}
    result_4 = process_api_call(status_4, data_4)
    print(f"\n--- Scenario 4 (Unknown Server Error) ---")
    print(result_4)
    status_5 = 200
    data_5 = None
    result_5 = process_api_call(status_5, data_5)
    print(f"\n--- Scenario 5 (Missing Data) ---")
    print(result_5)