def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    result = parts[0]
    for i in range(1, len(parts)):
        word = parts[i]
        if word:
            result += word[0].upper() + word[1:]
    return result

if __name__ == '__main__':
    test_cases = ["hello_world", "snake_case_to_camel_case", "single", "already_camelCase", "multiple___underscores", "trailing_"]
    for case in test_cases:
        converted = snake_to_camel(case)
        print(f"{case} -> {converted}")