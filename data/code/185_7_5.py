from urllib.parse import unquote

class URLQueryParser:
    @staticmethod
    def parse(query_string):
        result = {}
        pairs = query_string.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                decoded_key = unquote(key)
                decoded_value = unquote(value)
                URLQueryParser._update_result(result, decoded_key, decoded_value)
        return result

    @staticmethod
    def _update_result(result, key, value):
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value

if __name__ == '__main__':
    sample_query = 'a=1&a=2&b=3'
    parser = URLQueryParser()
    print(parser.parse(sample_query))