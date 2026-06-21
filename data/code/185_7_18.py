import urllib.parse

class QueryParser:
    def __init__(self):
        self.result = {}

    def parse_query_string(self, query_string):
        pairs = query_string.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                decoded_key = urllib.parse.unquote(key)
                decoded_value = urllib.parse.unquote(value)
                self._add_to_result(decoded_key, decoded_value)

    def _add_to_result(self, key, value):
        if key in self.result:
            if isinstance(self.result[key], list):
                self.result[key].append(value)
            else:
                self.result[key] = [self.result[key], value]
        else:
            self.result[key] = value

if __name__ == '__main__':
    parser = QueryParser()
    sample_query = 'a=1&a=2&b=3'
    parser.parse_query_string(sample_query)
    print(parser.result)