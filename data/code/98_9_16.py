def validate_response(status_code, data):
    if status_code == 200:
        return isinstance(data, dict) and 'result' in data
    elif status_code == 400:
        return isinstance(data, dict) and 'reason' in data
    elif status_code == 500:
        return isinstance(data, dict) and 'error_type' in data
    else:
        return False

def simulate_api_response(status_code, data):
    if not validate_response(status_code, data):
        return {"status": "error", "message": "Invalid response format"}

    if status_code == 200:
        if data['result'] == 'success':
            return {"status": "success", "message": "Data retrieved successfully", "payload": data['result']}
        else:
            return {"status": "error", "message": "API reported an internal failure", "details": data.get('error_details', 'Unknown error')}
    elif status_code == 400:
        return {"status": "client_error", "message": f"Bad Request: {data['reason']}"}
    elif status_code == 500:
        return {"status": "server_error", "message": f"Server failed: {data['error_type']}", "details": data.get('traceback', 'No traceback provided')}
    else:
        return {"status": "unknown_error", "message": f"Received unexpected status code: {status_code}"}

if __name__ == '__main__':
    sample_data_200 = {'result': 'success'}
    sample_data_400 = {'reason': 'Invalid input'}
    sample_data_500 = {'error_type': 'InternalError'}

    print(simulate_api_response(200, sample_data_200))
    print(simulate_api_response(400, sample_data_400))
    print(simulate_api_response(500, sample_data_500))