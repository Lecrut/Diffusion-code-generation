def handle_api_response(status_code, data):
    if status_code == 200:
        if 'error' in data:
            return f'Error: {data['error']}'
        else:
            return 'Success'
    elif status_code == 404:
        return 'Resource not found'
    elif status_code == 500:
        return 'Server error'
    else:
        return 'Unknown error'
if __name__ == '__main__':
    response1 = handle_api_response(200, {'data': 'some data'})
    print(response1)
    response2 = handle_api_response(404, {})
    print(response2)
    response3 = handle_api_response(500, {})
    print(response3)
    response4 = handle_api_response(400, {'error': 'invalid request'})
    print(response4)