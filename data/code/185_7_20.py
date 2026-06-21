def parse_query_string(query):
    result = {}
    pairs = query.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            key = unquote(key)
            value = unquote(value)
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value
    return result

if __name__ == '__main__':
    sample_query = 'foo=bar&baz=qux&foo=baz'
    print(parse_query_string(sample_query))