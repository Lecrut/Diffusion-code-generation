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
        elif s[pos] in 'truefalse':
            return parse_boolean()
        elif s[pos] == 'n':
            return parse_null()
        else:
            raise ValueError("Unexpected character")

    def skip_whitespace():
        nonlocal pos
        while pos < len(s) and s[pos].isspace():
            pos += 1

    def parse_object():
        nonlocal pos
        pos += 1
        obj = {}
        while pos < len(s):
            skip_whitespace()
            if s[pos] == '}':
                pos += 1
                break
            key = parse_string()
            skip_whitespace()
            if s[pos] != ':':
                raise ValueError("Expected ':'")
            pos += 1
            value = parse_value()
            obj[key] = value
            skip_whitespace()
            if s[pos] == ',':
                pos += 1
        return obj

    def parse_array():
        nonlocal pos
        pos += 1
        arr = []
        while pos < len(s):
            skip_whitespace()
            if s[pos] == ']':
                pos += 1
                break
            value = parse_value()
            arr.append(value)
            skip_whitespace()
            if s[pos] == ',':
                pos += 1
        return arr

    def parse_number():
        nonlocal pos
        start = pos
        while pos < len(s) and (s[pos].isdigit() or s[pos] in '.eE+-'):
            pos += 1
        return float(s[start:pos]) if '.' in s[start:pos] else int(s[start:pos])

    def parse_string():
        nonlocal pos
        start = pos + 1
        while pos < len(s) and s[pos] != '"':
            if s[pos] == '\\':
                pos += 2
            else:
                pos += 1
        if pos >= len(s):
            raise ValueError("Unterminated string")
        pos += 1
        return s[start:pos].replace('\\"', '"').replace('\\n', '\n')

    def parse_boolean():
        nonlocal pos
        start = pos
        while pos < len(s) and s[pos].isalpha():
            pos += 1
        if s[start:pos] == 'true':
            return True
        elif s[start:pos] == 'false':
            return False
        else:
            raise ValueError("Invalid boolean value")

    def parse_null():
        nonlocal pos
        start = pos
        while pos < len(s) and s[pos].isalpha():
            pos += 1
        if s[start:pos] == 'null':
            return None
        else:
            raise ValueError("Invalid null value")

    pos = 0
    skip_whitespace()
    result = parse_value()
    skip_whitespace()
    if pos < len(s):
        raise ValueError("Unexpected characters at the end")
    return result

if __name__ == '__main__':
    sample_json_like = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    print(parse_json_like(sample_json_like))