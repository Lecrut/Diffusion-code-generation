class JSONParser:
    QUOTATION_MARK = '"'
    LEFT_BRACE = '{'
    RIGHT_BRACE = '}'
    LEFT_BRACKET = '['
    RIGHT_BRACKET = ']'
    COMMA = ','
    COLON = ':'
    TRUE = 'true'
    FALSE = 'false'
    NULL = 'null'

    @staticmethod
    def parse(text_data):
        pos = 0

        def skip_whitespace():
            nonlocal pos
            while pos < len(text_data) and text_data[pos].isspace():
                pos += 1

        def parse_value():
            skip_whitespace()
            if text_data[pos] == JSONParser.LEFT_BRACE:
                return JSONParser.parse_object()
            elif text_data[pos] == JSONParser.LEFT_BRACKET:
                return JSONParser.parse_array()
            elif text_data[pos] == JSONParser.QUOTATION_MARK:
                return JSONParser.parse_string()
            elif text_data[pos].isdigit() or text_data[pos] == '-':
                return JSONParser.parse_number()
            elif text_data[pos] in 'tf':
                return JSONParser.parse_boolean()
            elif text_data[pos] == JSONParser.NULL[0]:
                return JSONParser.parse_null()

        def parse_object():
            nonlocal pos
            obj = {}
            pos += 1
            skip_whitespace()
            if text_data[pos] != JSONParser.RIGHT_BRACE:
                while True:
                    key = parse_value()
                    skip_whitespace()
                    if text_data[pos] != JSONParser.COLON:
                        raise ValueError("Expected ':'")
                    pos += 1
                    value = parse_value()
                    obj[key] = value
                    skip_whitespace()
                    if text_data[pos] == JSONParser.COMMA:
                        pos += 1
                    else:
                        break
            pos += 1
            return obj

        def parse_array():
            nonlocal pos
            arr = []
            pos += 1
            skip_whitespace()
            if text_data[pos] != JSONParser.RIGHT_BRACKET:
                while True:
                    value = parse_value()
                    arr.append(value)
                    skip_whitespace()
                    if text_data[pos] == JSONParser.COMMA:
                        pos += 1
                    else:
                        break
            pos += 1
            return arr

        def parse_string():
            nonlocal pos
            start = pos
            pos += 1
            while pos < len(text_data) and text_data[pos] != JSONParser.QUOTATION_MARK:
                if text_data[pos] == '\\':
                    pos += 2
                else:
                    pos += 1
            if pos >= len(text_data):
                raise ValueError("Unterminated string")
            result = text_data[start + 1 : pos]
            pos += 1
            return result

        def parse_number():
            nonlocal pos
            start = pos
            while pos < len(text_data) and (text_data[pos].isdigit() or text_data[pos] in '.eE+-'):
                pos += 1
            return float(text_data[start : pos])

        def parse_boolean():
            nonlocal pos
            if text_data[pos : pos + 4] == JSONParser.TRUE:
                pos += 4
                return True
            elif text_data[pos : pos + 5] == JSONParser.FALSE:
                pos += 5
                return False
            else:
                raise ValueError("Expected 'true' or 'false'")

        def parse_null():
            nonlocal pos
            if text_data[pos : pos + 4] == JSONParser.NULL:
                pos += 4
                return None
            else:
                raise ValueError("Expected 'null'")

        return parse_value()

if __name__ == '__main__':
    parser = JSONParser()
    sample_text = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": null}'
    parsed_data = parser.parse(sample_text)
    print(parsed_data)