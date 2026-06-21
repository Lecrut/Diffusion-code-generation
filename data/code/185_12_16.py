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
        elif s[pos] == 't' and s[pos:pos+4] == 'true':
            pos += 4
            return True
        elif s[pos] == 'f' and s[pos:pos+5] == 'false':
            pos += 5
            return False
        elif s[pos] == 'n' and s[pos:pos+4] == 'null':
            pos += 4
            return None

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

    def parse_number():
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

    def parse_string():
        nonlocal pos
        start = pos + 1
        while s[pos] != '"':
            pos += 1
        pos += 1
        return s[start:pos]

    pos = 0
    return parse_value()

if __name__ == '__main__':
    sample_json_like = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    print(parse_json_like(sample_json_like))