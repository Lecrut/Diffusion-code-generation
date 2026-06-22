def snake_to_camel(s):
    if not s:
        return s
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel('this_is_a_snake_case_string')
    print(result)