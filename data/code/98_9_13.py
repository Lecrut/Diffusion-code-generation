def handle_api_response(response):
    if response is None:
        return "Error: No response received"
    
    if not isinstance(response, dict):
        return "Error: Invalid response format"
    
    status_code = response.get('status')
    
    if status_code == 200:
        data = response.get('data')
        
        if data is None:
            return "Error: Missing data in response"
        
        if not isinstance(data, list):
            return "Error: Data must be a list"
        
        if len(data) == 0:
            return "Warning: Empty data list received"
        
        for item in data:
            if not isinstance(item, dict):
                return "Error: Each item in data must be a dictionary"
            
            if 'id' not in item or 'name' not in item:
                return "Error: Missing id or name in data item"
        
        return "Success: Valid response received"
    
    elif status_code == 404:
        return "Error: Resource not found"
    
    elif status_code == 500:
        return "Error: Internal server error"
    
    else:
        return f"Warning: Unknown status code {status_code}"

if __name__ == '__main__':
    sample_response = {
        'status': 200,
        'data': [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'}
        ]
    }
    
    print(handle_api_response(sample_response))