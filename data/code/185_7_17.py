def parse_query_string(query):
    result = {}
    pairs = query.split('&')
    for pair in pairs:
        key, value = pair.split('=', 1) if '=' in pair else (pair, '')
        decoded_key = decode_percent(key)
        decoded_value = decode_percent(value)
        if decoded_key in result:
            if isinstance(result[decoded_key], list):
                result[decoded_key].append(decoded_value)
            else:
                result[decoded_key] = [result[decoded_key], decoded_value]
        else:
            result[decoded_key] = decoded_value
    return result

def decode_percent(s):
    return s.replace('%20', ' ').replace('%21', '!').replace('%22', '"').replace('%23', '#') \
           .replace('%24', '$').replace('%25', '%').replace('%26', '&').replace('%27', "'") \
           .replace('%28', '(').replace('%29', ')').replace('%2A', '*').replace('%2B', '+') \
           .replace('%2C', ',').replace('%2F', '/').replace('%3A', ':').replace('%3B', ';') \
           .replace('%3D', '=').replace('%3F', '?').replace('%40', '@').replace('%5B', '[') \
           .replace('%5D', ']')

if __name__ == '__main__':
    sample_query = 'a=1&a=2&b=c%20d&e=f%26g'
    print(parse_query_string(sample_query))