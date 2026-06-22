def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if not parts:
        return ""
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    test_cases = ['hello_world', 'user_profile_data', 'convert_this_string', 'single', 'multiple___underscores', '']
    for case in test_cases:
        print(f"{case} -> {snake_to_camel(case)}")