import urllib.parse

class QueryParser:
    @staticmethod
    def parse_query_string(query):
        result = {}
        pairs = query.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                decoded_key = urllib.parse.unquote(key)
                decoded_value = urllib.parse.unquote(value)
                QueryParser._add_to_dict(result, decoded_key, decoded_value)
        return result

    @staticmethod
    def _add_to_dict(dictionary, key, value):
        if key in dictionary:
            if isinstance(dictionary[key], list):
                dictionary[key].append(value)
            else:
                dictionary[key] = [dictionary[key], value]
        else:
            dictionary[key] = value

if __name__ == '__main__':
    sample_query = 'a=1&a=2&b=3'
    parser = QueryParser()
    print(parser.parse_query_string(sample_query))