def simulate_api_response(status_code, data):
    if status_code == 200:
        if data is not None and isinstance(data, dict) and 'status' in data:
            if data['status'] == 'success':
                return {"outcome": "success", "note": "Data retrieval successful", "content": data.get('data', {})}
            else:
                return {"outcome": "error", "note": "API reported an internal failure", "details": data.get('error_message', 'Unknown error')}
        else:
            return {"outcome": "error", "note": "Invalid data format received", "details": "Missing 'status' key or data is not a dictionary"}
    elif status_code == 400:
        if 'message' in data:
            return {"outcome": "client_error", "note": f"Bad Request: {data['message']}"}
        else:
            return {"outcome": "client_error", "note": "Bad Request: Unknown message"}
    elif status_code == 500:
        if 'error_type' in data:
            return {"outcome": "server_error", "note": f"Server failed: {data['error_type']}", "details": data.get('stack_trace', 'No stack trace provided')}
        else:
            return {"outcome": "server_error", "note": "Server failed: Unknown error type", "details": "No stack trace provided"}
    else:
        return {"outcome": "unknown_error", "note": f"Received unexpected status code: {status_code}"}

if __name__ == '__main__':
    sample_response_200 = {'status': 'success', 'data': {'key': 'value'}}
    print(simulate_api_response(200, sample_response_200))

    sample_response_400 = {'message': 'Invalid input'}
    print(simulate_api_response(400, sample_response_400))

    sample_response_500 = {'error_type': 'DatabaseError', 'stack_trace': 'Traceback...'}
    print(simulate_api_response(500, sample_response_500))