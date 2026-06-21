def parse_json_like(s):

    def parse_value():
        if s[pos] == '{':
            return parse_object()
        elif s[pos] == '[':
            return parse_array()
        elif s[pos] in '"\'':
            return parse_string()
        elif s[pos].isdigit() or s[pos] == '-':
            return parse_number()
        elif s[pos] is True:
            pos += 4
            return True
        elif s[pos] is False:
            pos += 5
            return False
        elif s[pos] is None:
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

    def parse_string():
        nonlocal pos
        quote = s[pos]
        pos += 1
        result = []
        while s[pos] != quote:
            if s[pos] == '\\':
                pos += 1
                if s[pos] in '"\\/bfnrt':
                    result.append(s[pos])
                elif s[pos] == 'u':
                    result.append(chr(int(s[pos + 1:pos + 5], 16)))
                else:
                    raise ValueError('Invalid escape sequence')
            else:
                result.append(s[pos])
            pos += 1
        pos += 1
        return ''.join(result)

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
        if s[start] == '0' and start < pos - 1:
            raise ValueError('Leading zeros not allowed')
        return float(s[start:pos])
    pos = 0
    return parse_value()
if __name__ == '__main__':
    sample_json_like = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    print(parse_json_like(sample_json_like))