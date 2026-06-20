def handle_api_response(status_code, data):
    if status_code == 200:
        if 'error' in data:
            return f"Error: {data['error']}"
        else:
            return f"Success: {data['result']}"
    elif status_code == 404:
        return "Error: Resource not found"
    elif status_code == 500:
        return "Error: Internal server error"
    else:
        return f"Unknown error with status code: {status_code}"

if __name__ == '__main__':
    response1 = handle_api_response(200, {'result': 'Data fetched successfully'})
    print(response1)
    
    response2 = handle_api_response(404, {})
    print(response2)
    
    response3 = handle_api_response(500, {})
    print(response3)
    
    response4 = handle_api_response(403, {'error': 'Permission denied'})
    print(response4)