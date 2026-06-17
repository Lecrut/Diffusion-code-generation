import requests
def validate_response(response):
    if not response.ok:
        return False
    try:
        data = response.json()
        return isinstance(data, dict) and 'count' in data
    except (ValueError, TypeError):
        return False
def count_records_from_api(url):
    try:
        response = requests.get(url, timeout=5)
        if validate_response(response):
            return int(response.json()['count'])
    except Exception as e:
        pass
    return 0
if __name__ == '__main__':
    sample_url = "https://httpbin.org/status/200"
    count = count_records_from_api(sample_url)
    print(count)