def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    first_part = parts[0]
    rest_parts = []
    for part in parts[1:]:
        if part:
            rest_parts.append(part[0].upper() + part[1:])
    return first_part + ''.join(rest_parts)

if __name__ == '__main__':
    sample_values = [
        "hello_world",
        "snake_case_identifier",
        "single",
        "multiple___underscores",
        "already_Camel",
        "trailing_",
        "_leading",
        "",
        "a_b_c_d",
        "simple"
    ]
    for val in sample_values:
        print(snake_to_camel(val))