def to_camel_case(snake_str):
    if not isinstance(snake_str, str):
        raise TypeError("Input must be a string")
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if not any(parts):
        return snake_str
    first_part = parts[0]
    if not first_part:
        return "".join(part.capitalize() if part else "" for part in parts)
    result = [first_part.lower()]
    for part in parts[1:]:
        if part:
            result.append(part.capitalize())
        else:
            result.append("")
    return "".join(result)

if __name__ == '__main__':
    sample_cases = ["user_name", "first_name", "http_status_code", "single", "alreadyCamelCase", "_leading_underscore", "trailing_underscore_", "__double__underscores__"]
    for case in sample_cases:
        print(f"{case} -> {to_camel_case(case)}")