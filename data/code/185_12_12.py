def parse_json_like(s):
    def parse_value():
        if s[pos] == '{':
            return parse_object()
        elif s[pos] == '[':
            return parse_array()
        elif s[pos].isdigit() or s[pos] == '-':
            return parse_number()
        elif s[pos] == '"':
            return parse_string()
        elif s[pos] in 'tfn':
            return parse_boolean_or_null()
        else:
            raise ValueError("Unexpected character: " + s[pos])

    def parse_object():
        pos += 1
        obj = {}
        while s[pos] != '}':
            key = parse_string()
            pos += 1
            value = parse_value()
            obj[key] = value
            if s[pos] == ',':
                pos += 1
        pos += 1
        return obj

    def parse_array():
        pos += 1
        arr = []
        while s[pos] != ']':
            value = parse_value()
            arr.append(value)
            if s[pos] == ',':
                pos += 1
        pos += 1
        return arr

    def parse_number():
        start = pos
        if s[pos] == '-':
            pos += 1
        while pos < len(s) and (s[pos].isdigit() or s[pos] == '.'):
            pos += 1
        num_str = s[start:pos]
        try:
            return int(num_str)
        except ValueError:
            return float(num_str)

    def parse_string():
        pos += 1
        start = pos
        while pos < len(s) and s[pos] != '"':
            if s[pos] == '\\':
                pos += 2
            else:
                pos += 1
        string = s[start:pos]
        pos += 1
        return string

    def parse_boolean_or_null():
        start = pos
        while pos < len(s) and s[pos].isalpha():
            pos += 1
        token = s[start:pos]
        if token == 'true':
            return True
        elif token == 'false':
            return False
        elif token == 'null':
            return None
        else:
            raise ValueError("Unexpected token: " + token)

    global pos
    pos = 0
    return parse_value()

if __name__ == '__main__':
    json_like_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    result = parse_json_like(json_like_string)
    print(result)