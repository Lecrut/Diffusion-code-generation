def simulate_api_response(status_code, data):
    if status_code == 200:
        if isinstance(data, dict) and 'status' in data:
            if data['status'] == 'success':
                return {"status": "success", "message": "Data retrieved successfully", "payload": data.get('data', None)}
            else:
                return {"status": "error", "message": "API reported an internal failure", "details": data.get('error_details', 'Unknown error')}
        else:
            return {"status": "error", "message": "Invalid response format received", "details": "Missing 'status' key or data is not a dictionary"}
    elif status_code == 401:
        if isinstance(data, dict) and 'reason' in data:
            return {"status": "client_error", "message": f"Unauthorized: {data['reason']}"}
        else:
            return {"status": "client_error", "message": "Unauthorized: Unknown reason"}
    elif status_code == 403:
        if isinstance(data, dict) and 'permission' in data:
            return {"status": "client_error", "message": f"Forbidden: {data['permission']}"}
        else:
            return {"status": "client_error", "message": "Forbidden: Access denied"}
    elif status_code == 503:
        if isinstance(data, dict) and 'service' in data:
            return {"status": "server_error", "message": f"Service Unavailable: {data['service']}", "details": data.get('error', 'No error provided')}
        else:
            return {"status": "server_error", "message": "Service Unavailable: Backend service is down"}
    else:
        return {"status": "unknown_error", "message": f"Received unexpected status code: {status_code}"}

if __name__ == '__main__':
    response = simulate_api_response(200, {'status': 'success', 'data': 'Sample data'})
    print(response)

    response = simulate_api_response(401, {'reason': 'Invalid token'})
    print(response)

    response = simulate_api_response(403, {'permission': 'No access rights'})
    print(response)

    response = simulate_api_response(503, {'service': 'Database', 'error': 'Connection failed'})
    print(response)