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
        elif s[pos] in 'tf':
            return parse_boolean()
        elif s[pos] == 'n':
            return parse_null()
        else:
            raise ValueError('Unexpected character: ' + s[pos])

    def parse_object():
        nonlocal pos
        pos += 1
        obj = {}
        while s[pos] != '}':
            key = parse_string()
            pos += 2
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
        start = pos + 1
        while s[pos] != '"':
            pos += 1
        end = pos
        pos += 1
        return s[start:end]

    def parse_number():
        nonlocal pos
        start = pos
        if s[pos] == '-':
            pos += 1
        while s[pos].isdigit():
            pos += 1
        if s[pos] == '.':
            pos += 1
            while s[pos].isdigit():
                pos += 1
        return float(s[start:pos]) if '.' in s[start:pos] else int(s[start:pos])

    def parse_boolean():
        nonlocal pos
        if s[pos:].startswith('true'):
            pos += 4
            return True
        elif s[pos:].startswith('false'):
            pos += 5
            return False
        else:
            raise ValueError('Unexpected boolean value')

    def parse_null():
        nonlocal pos
        if s[pos:].startswith('null'):
            pos += 4
            return None
        else:
            raise ValueError('Unexpected null value')
    pos = 0
    return parse_value()
if __name__ == '__main__':
    json_like_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    result = parse_json_like(json_like_string)
    print(result)