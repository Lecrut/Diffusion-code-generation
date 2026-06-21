def parse_json_like(s):
    def parse_value():
        if s[pos] == '{':
            return parse_object()
        elif s[pos] == '[':
            return parse_array()
        elif s[pos] == '"':
            return parse_string()
        elif s[pos].isdigit() or s[pos] == '-':
            return parse_number()
        elif s[pos] in 'tfn':
            return parse_boolean_or_null()
        else:
            raise ValueError("Unexpected character: " + s[pos])

    def parse_object():
        nonlocal pos
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
        nonlocal pos
        pos += 1
        arr = []
        while s[pos] != ']':
            value = parse_value()
            arr.append(value)
            if s[pos] == ',':
                pos += 1
        pos += 1
        return arr

    def parse_string():
        nonlocal pos
        start = pos
        pos += 1
        while s[pos] != '"':
            if s[pos] == '\\':
                pos += 2
            else:
                pos += 1
        result = s[start + 1 : pos]
        pos += 1
        return result

    def parse_number():
        nonlocal pos
        start = pos
        while pos < len(s) and (s[pos].isdigit() or s[pos] in '.eE+-'):
            pos += 1
        return float(s[start:pos])

    def parse_boolean_or_null():
        nonlocal pos
        if s[pos : pos + 4] == 'true':
            pos += 4
            return True
        elif s[pos : pos + 5] == 'false':
            pos += 5
            return False
        elif s[pos : pos + 4] == 'null':
            pos += 4
            return None
        else:
            raise ValueError("Unexpected character: " + s[pos])

    pos = 0
    return parse_value()

if __name__ == '__main__':
    sample_json_like = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    print(parse_json_like(sample_json_like))