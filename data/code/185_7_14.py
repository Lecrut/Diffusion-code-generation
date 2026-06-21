import urllib.parse

class QueryParser:
    @staticmethod
    def parse(query_string):
        result = {}
        pairs = query_string.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                decoded_key = urllib.parse.unquote(key)
                decoded_value = urllib.parse.unquote(value)
                QueryParser._add_to_dict(result, decoded_key, decoded_value)
        return result

    @staticmethod
    def _add_to_dict(result, key, value):
        if key in result:
            if isinstance(result[key], list):
                result[key].append(decoded_value)
            else:
                result[key] = [result[key], decoded_value]
        else:
            result[key] = decoded_value

if __name__ == '__main__':
    sample_query = 'a=1&a=2&b=3'
    parser = QueryParser()
    print(parser.parse(sample_query))