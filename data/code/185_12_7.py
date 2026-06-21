def parse_json_like(s):
    def skip_whitespace():
        nonlocal i
        while i < len(s) and s[i].isspace():
            i += 1

    def parse_value():
        skip_whitespace()
        if s[i] == '{':
            return parse_object()
        elif s[i] == '[':
            return parse_array()
        elif s[i] == '"':
            return parse_string()
        elif s[i].isdigit() or s[i] == '-':
            return parse_number()
        elif s[i] in 'truefalse':
            return parse_boolean()
        elif s[i] == 'n':
            return parse_null()

    def parse_object():
        nonlocal i
        i += 1
        obj = {}
        while i < len(s) and s[i] != '}':
            key = parse_string()
            skip_whitespace()
            if s[i] != ':':
                raise ValueError("Expected ':' after key")
            i += 1
            value = parse_value()
            obj[key] = value
            skip_whitespace()
            if s[i] == ',':
                i += 1
        if s[i] != '}':
            raise ValueError("Expected '}' at end of object")
        i += 1
        return obj

    def parse_array():
        nonlocal i
        i += 1
        arr = []
        while i < len(s) and s[i] != ']':
            value = parse_value()
            arr.append(value)
            skip_whitespace()
            if s[i] == ',':
                i += 1
        if s[i] != ']':
            raise ValueError("Expected ']' at end of array")
        i += 1
        return arr

    def parse_string():
        nonlocal i
        if s[i] != '"':
            raise ValueError("Expected string to start with '\"'")
        i += 1
        start = i
        while i < len(s) and s[i] != '"':
            i += 1
        if i == len(s):
            raise ValueError("Unterminated string")
        value = s[start:i]
        i += 1
        return value

    def parse_number():
        nonlocal i
        start = i
        while i < len(s) and (s[i].isdigit() or s[i] in '.+-eE'):
            i += 1
        value = float(s[start:i]) if '.' in s[start:i] else int(s[start:i])
        return value

    def parse_boolean():
        nonlocal i
        if s[i:i+4] == 'true':
            i += 4
            return True
        elif s[i:i+5] == 'false':
            i += 5
            return False
        else:
            raise ValueError("Expected boolean value")

    def parse_null():
        nonlocal i
        if s[i:i+4] == 'null':
            i += 4
            return None
        else:
            raise ValueError("Expected null value")

    i = 0
    return parse_value()

if __name__ == '__main__':
    json_like_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    result = parse_json_like(json_like_string)
    print(result)