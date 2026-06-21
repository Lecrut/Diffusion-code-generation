def parse_json_like(s):
    stack = []
    current_value = ''
    result = {}
    key = None

    for char in s:
        if char == '{':
            if current_value:
                if key is not None:
                    result[key] = eval(current_value)
                    key = None
                else:
                    raise ValueError("Unexpected value before object start")
                current_value = ''
            stack.append(result)
            result = {}
        elif char == '}':
            if current_value:
                if key is not None:
                    result[key] = eval(current_value)
                    key = None
                else:
                    raise ValueError("Unexpected value before object end")
                current_value = ''
            parent = stack.pop()
            parent[stack[-1]] = result
            result = parent
        elif char == '[':
            if current_value:
                if key is not None:
                    result[key] = eval(current_value)
                    key = None
                else:
                    raise ValueError("Unexpected value before array start")
                current_value = ''
            stack.append(result)
            result = []
        elif char == ']':
            if current_value:
                if key is not None:
                    result.append(eval(current_value))
                    key = None
                else:
                    raise ValueError("Unexpected value before array end")
                current_value = ''
            parent = stack.pop()
            parent[stack[-1]] = result
            result = parent
        elif char == ',':
            if current_value:
                if key is not None:
                    result[key] = eval(current_value)
                    key = None
                else:
                    raise ValueError("Unexpected value before comma")
                current_value = ''
            else:
                raise ValueError("Empty string before comma")
        elif char == ':':
            if current_value:
                key = current_value.strip()
                current_value = ''
            else:
                raise ValueError("Empty string before colon")
        elif char == '"':
            if current_value and current_value[0] != '"':
                current_value += char
            else:
                if key is None:
                    key = current_value.strip('"')
                else:
                    result[key] = current_value.strip('"')
                current_value = ''
        elif char.isdigit() or char in '-.eE':
            current_value += char
        elif char == 't' and current_value == 'true':
            if key is not None:
                result[key] = True
                key = None
            else:
                raise ValueError("Unexpected true before value")
            current_value = ''
        elif char == 'f' and current_value == 'false':
            if key is not None:
                result[key] = False
                key = None
            else:
                raise ValueError("Unexpected false before value")
            current_value = ''
        elif char == 'n' and current_value == 'null':
            if key is not None:
                result[key] = None
                key = None
            else:
                raise ValueError("Unexpected null before value")
            current_value = ''

    return result

if __name__ == '__main__':
    sample_json_like = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    print(parse_json_like(sample_json_like))