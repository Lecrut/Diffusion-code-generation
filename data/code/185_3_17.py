import re

class JSONParser:
    _TOKEN_RE = '\\s*(\\{|\\}|\\[|\\]|\\:|\\,|"[^"]*")\\s*'

    @staticmethod
    def parse(json_string):
        tokens = re.findall(JSONParser._TOKEN_RE, json_string)
        result = JSONParser._parse_value(tokens)
        return result

    @staticmethod
    def _parse_value(tokens):
        token = tokens.pop(0)
        if token == '{':
            return JSONParser._parse_dict(tokens)
        elif token == '[':
            return JSONParser._parse_list(tokens)
        elif token[0] == '"':
            return token[1:-1]
        else:
            try:
                return int(token)
            except ValueError:
                raise ValueError(f'Invalid value: {token}')

    @staticmethod
    def _parse_dict(tokens):
        result = {}
        while True:
            key = JSONParser._parse_value(tokens)
            if key == '}':
                break
            tokens.pop(0)
            value = JSONParser._parse_value(tokens)
            result[key] = value
        return result

    @staticmethod
    def _parse_list(tokens):
        result = []
        while True:
            value = JSONParser._parse_value(tokens)
            if value == ']':
                break
            result.append(value)
        return result
if __name__ == '__main__':
    sample_string = '{"a": 10, "b": [25, 30], "c": {"d": 45}}'
    parsed_data = JSONParser.parse(sample_string)
    print(parsed_data)