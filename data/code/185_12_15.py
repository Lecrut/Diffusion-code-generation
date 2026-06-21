class JsonParser:
    def parse(self, text_data):
        pos = 0
        length = len(text_data)

        def skip_whitespace():
            nonlocal pos
            while pos < length and text_data[pos].isspace():
                pos += 1

        def parse_value():
            skip_whitespace()
            if pos >= length:
                raise ValueError("Unexpected end of string")
            char = text_data[pos]
            if char == '{':
                return parse_object()
            elif char == '[':
                return parse_array()
            elif char == '"':
                return parse_string()
            elif char.isdigit() or char == '-':
                return parse_number()
            elif char in 'tf':
                return parse_boolean()
            elif char == 'n':
                return parse_null()
            else:
                raise ValueError(f"Unexpected character: {char}")

        def parse_object():
            nonlocal pos
            obj = {}
            pos += 1
            skip_whitespace()
            if text_data[pos] == '}':
                pos += 1
                return obj
            while True:
                key = parse_string()
                skip_whitespace()
                if text_data[pos] != ':':
                    raise ValueError("Expected ':'")
                pos += 1
                value = parse_value()
                obj[key] = value
                skip_whitespace()
                if text_data[pos] == ',':
                    pos += 1
                else:
                    break
            if text_data[pos] != '}':
                raise ValueError("Expected '}'")
            pos += 1
            return obj

        def parse_array():
            nonlocal pos
            arr = []
            pos += 1
            skip_whitespace()
            if text_data[pos] == ']':
                pos += 1
                return arr
            while True:
                value = parse_value()
                arr.append(value)
                skip_whitespace()
                if text_data[pos] == ',':
                    pos += 1
                else:
                    break
            if text_data[pos] != ']':
                raise ValueError("Expected ']'")
            pos += 1
            return arr

        def parse_string():
            nonlocal pos
            if text_data[pos] != '"':
                raise ValueError("Expected string to start with '\"'")
            pos += 1
            result = []
            while True:
                if pos >= length or text_data[pos] == '"':
                    break
                elif text_data[pos] == '\\':
                    pos += 1
                    if pos >= length:
                        raise ValueError("Unexpected end of string after escape character")
                    char = text_data[pos]
                    if char in ('"', '\\', '/', 'b', 'f', 'n', 'r', 't'):
                        result.append(char)
                    elif char == 'u':
                        if pos + 4 >= length or not all(c.isdigit() for c in text_data[pos+1:pos+5]):
                            raise ValueError("Invalid Unicode escape sequence")
                        pos += 4
                        result.append(chr(int(text_data[pos-4:pos], 16)))
                    else:
                        raise ValueError(f"Unsupported escape character: {char}")
                else:
                    result.append(text_data[pos])
                pos += 1
            if pos >= length or text_data[pos] != '"':
                raise ValueError("Expected string to end with '\"'")
            pos += 1
            return ''.join(result)

        def parse_number():
            nonlocal pos
            start = pos
            while pos < length and (text_data[pos].isdigit() or text_data[pos] in '.eE+-'):
                pos += 1
            num_str = text_data[start:pos]
            if '.' in num_str:
                return float(num_str)
            else:
                return int(num_str)

        def parse_boolean():
            nonlocal pos
            if text_data[pos:pos+4] == 'true':
                pos += 4
                return True
            elif text_data[pos:pos+5] == 'false':
                pos += 5
                return False
            else:
                raise ValueError("Expected boolean value")

        def parse_null():
            nonlocal pos
            if text_data[pos:pos+4] == 'null':
                pos += 4
                return None
            else:
                raise ValueError("Expected null value")

        return parse_value()

if __name__ == '__main__':
    parser = JsonParser()
    sample_json = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"]}'
    result = parser.parse(sample_json)
    print(result)