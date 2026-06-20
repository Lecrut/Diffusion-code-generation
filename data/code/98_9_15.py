def handle_api_response(response):
    if response is None:
        return "Error: No response received"
    
    status_code = response.get('status_code')
    data = response.get('data')

    if status_code == 200:
        if 'error' in data:
            error_type = data['error']['type']
            if error_type == 'timeout':
                return "Error: Request timed out"
            elif error_type == 'not_found':
                return "Error: Resource not found"
            else:
                return f"Error: Unknown error type {error_type}"
        else:
            return "Success: Data retrieved successfully"
    elif status_code == 401:
        return "Error: Unauthorized access"
    elif status_code == 500:
        return "Error: Internal server error"
    else:
        return f"Error: Unknown HTTP status code {status_code}"

if __name__ == '__main__':
    sample_response = {
        'status_code': 200,
        'data': {
            'error': {
                'type': 'timeout'
            }
        }
    }
    print(handle_api_response(sample_response))