def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0].lower()
    result = parts[0].lower()
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:].lower()
    return result

if __name__ == '__main__':
    sample_strings = ["hello_world", "this_is_a_test_case", "snake_case", "alreadyCamel", "a_b_c"]
    for s in sample_strings:
        print(snake_to_camel(s))