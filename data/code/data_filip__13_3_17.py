def snake_to_camel(s):
    if not s:
        return ""
    parts = s.split("_")
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    sample_input = "this_is_a_snake_case_string"
    output = snake_to_camel(sample_input)
    print(output)