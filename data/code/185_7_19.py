from urllib.parse import unquote

def is_valid_query_string(query_string):
    if not isinstance(query_string, str) or '=' not in query_string:
        return False
    return True

def parse_url_query(query_string):
    if not is_valid_query_string(query_string):
        raise ValueError("Invalid query string format")

    result = {}
    pairs = query_string.split('&')
    for pair in pairs:
        key, value = pair.split('=', 1) if '=' in pair else (pair, '')
        decoded_key = unquote(key)
        decoded_value = unquote(value)
        if decoded_key in result:
            if isinstance(result[decoded_key], list):
                result[decoded_key].append(decoded_value)
            else:
                result[decoded_key] = [result[decoded_key], decoded_value]
        else:
            result[decoded_key] = decoded_value
    return result

if __name__ == '__main__':
    sample_query = 'a=1&a=2&b=3'
    print(parse_url_query(sample_query))