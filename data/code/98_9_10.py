def handle_api_response(response):
    if response is None:
        return "Error: No response received"
    
    status_code = response.get('status_code')
    data = response.get('data')

    if status_code == 200:
        if data is not None:
            return f"Success: Data received - {data}"
        else:
            return "Error: Response data is empty"
    elif status_code == 404:
        return "Error: Resource not found"
    elif status_code == 500:
        return "Error: Internal server error"
    else:
        return f"Error: Unknown status code - {status_code}"

if __name__ == '__main__':
    sample_response = {
        'status_code': 200,
        'data': {'key': 'value'}
    }
    print(handle_api_response(sample_response))