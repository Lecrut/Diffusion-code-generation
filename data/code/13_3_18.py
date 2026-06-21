def to_camel_case(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

if __name__ == '__main__':
    sample_cases = ["hello_world", "user_profile_data", "snake_case_to_camel_case", "single", "alreadyCamelCase"]
    for s in sample_cases:
        print(to_camel_case(s))