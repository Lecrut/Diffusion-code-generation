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
        while True:
            if s[pos] == '}':
                pos += 1
                break
            key = parse_string()
            pos += 1
            value = parse_value()
            obj[key] = value
            if s[pos] == ',':
                pos += 1
        return obj

    def parse_array():
        nonlocal pos
        pos += 1
        arr = []
        while True:
            if s[pos] == ']':
                pos += 1
                break
            value = parse_value()
            arr.append(value)
            if s[pos] == ',':
                pos += 1
        return arr

    def parse_string():
        nonlocal pos
        pos += 1
        start = pos
        while s[pos] != '"':
            pos += 1
        result = s[start:pos]
        pos += 1
        return result

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
        result = float(s[start:pos]) if '.' in s[start:pos] else int(s[start:pos])
        return result

    pos = 0
    return parse_value()

if __name__ == '__main__':
    json_like_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    result = parse_json_like(json_like_string)
    print(result)