def simulate_api_response(status_code, data):
    if status_code == 200:
        if isinstance(data, dict) and 'error' not in data:
            return {"success": True, "result": data}
        else:
            return {"success": False, "error_type": "MalformedData", "message": "Data structure invalid"}
    elif status_code == 400:
        if 'invalid_field' in data:
            return {"success": False, "error_type": "ValidationError", "message": f"Validation failed for field: {data.get('invalid_field', 'unknown')}"}
        else:
            return {"success": False, "error_type": "BadRequest", "message": "Request parameters were invalid"}
    elif status_code == 500:
        if 'database_down' in data:
            return {"success": False, "error_type": "ServiceUnavailable", "message": "The backend service is currently unavailable"}
        else:
            return {"success": False, "error_type": "InternalServerError", "message": "An unexpected server error occurred"}
    else:
        return {"success": False, "error_type": "UnknownError", "message": f"Received unexpected status code: {status_code}"}
if __name__ == '__main__':
    response1 = simulate_api_response(200, {"id": 1, "value": 100})
    print("--- Response 1 (Success) ---")
    print(response1)
    response2 = simulate_api_response(200, {"id": 2, "error": "Internal"} )
    print("\n--- Response 2 (Malformed Data) ---")
    print(response2)
    response3 = simulate_api_response(400, {"invalid_field": "test"})
    print("\n--- Response 3 (Validation Error) ---")
    print(response3)
    response4 = simulate_api_response(400, {"some_other_field": "test"})
    print("\n--- Response 4 (Bad Request) ---")
    print(response4)
    response5 = simulate_api_response(500, {"database_down": True})
    print("\n--- Response 5 (Service Unavailable) ---")
    print(response5)
    response6 = simulate_api_response(500, {"some_other_field": "test"})
    print("\n--- Response 6 (Internal Server Error) ---")
    print(response6)
    response7 = simulate_api_response(418, {"status": "NotImplemented"})
    print("\n--- Response 7 (Unknown Error) ---")
    print(response7)