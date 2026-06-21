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
            key = parse_string()
            if key is None:
                break
            pos += 1
            value = parse_value()
            obj[key] = value
            if s[pos] == ',':
                pos += 1
            else:
                break
        pos += 1
        return obj

    def parse_array():
        nonlocal pos
        pos += 1
        arr = []
        while True:
            value = parse_value()
            arr.append(value)
            if s[pos] == ',':
                pos += 1
            else:
                break
        pos += 1
        return arr

    def parse_string():
        nonlocal pos
        if s[pos] != '"':
            return None
        pos += 1
        start = pos
        while pos < len(s) and s[pos] != '"':
            pos += 1
        if pos == len(s):
            return None
        string = s[start:pos]
        pos += 1
        return string

    def parse_number():
        nonlocal pos
        start = pos
        if s[pos] == '-':
            pos += 1
        while pos < len(s) and (s[pos].isdigit() or s[pos] == '.'):
            pos += 1
        number_str = s[start:pos]
        try:
            return int(number_str)
        except ValueError:
            return float(number_str)

    pos = 0
    return parse_value()

if __name__ == '__main__':
    json_like_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": null}}'
    result = parse_json_like(json_like_string)
    print(result)