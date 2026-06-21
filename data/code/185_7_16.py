def parse_query_string(query):
    result = {}
    pairs = query.split('&')
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
    sample_query = 'foo=bar&baz=qux&foo=baz'
    print(parse_query_string(sample_query))