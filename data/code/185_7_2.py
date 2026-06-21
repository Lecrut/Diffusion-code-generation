def parse_query_string(query):
    result = {}
    pairs = query.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
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
    sample_query = 'name=John&age=30&hobbies=reading&hobbies=cycling'
    print(parse_query_string(sample_query))