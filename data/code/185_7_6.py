import urllib.parse

def parse_url_query(query_string):
    result = {}
    pairs = query_string.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            decoded_key = urllib.parse.unquote(key)
            decoded_value = urllib.parse.unquote(value)
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