def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    result_parts = [parts[0].lower()]
    for part in parts[1:]:
        if part:
            result_parts.append(part[0].upper() + part[1:].lower())
        else:
            result_parts.append('')
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_input = "example_snake_case_string"
    converted_output = snake_to_camel(sample_input)
    print(converted_output)