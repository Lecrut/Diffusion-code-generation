def handle_api_response(response):
    if response is None:
        return "Error: No response received"
    
    status_code = response.get('status_code')
    if status_code is None:
        return "Error: Missing status code in response"
    
    if status_code == 200:
        data = response.get('data')
        if data is None:
            return "Error: Missing data in response"
        
        if 'error' in data:
            error_message = data['error']
            if error_message == "Invalid request":
                return "Error: Invalid request received"
            elif error_message == "Resource not found":
                return "Error: Resource not found"
            else:
                return f"Error: Unknown error - {error_message}"
        
        return "Success: Data retrieved successfully"
    
    elif status_code == 401:
        return "Error: Unauthorized access"
    
    elif status_code == 500:
        return "Error: Internal server error"
    
    else:
        return f"Error: Unknown HTTP status code - {status_code}"

if __name__ == '__main__':
    sample_response = {
        'status_code': 200,
        'data': {
            'error': 'Invalid request'
        }
    }
    print(handle_api_response(sample_response))