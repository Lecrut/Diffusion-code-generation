def to_camel_case(snake_str: str) -> str:
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "convert_snake_case_to_camel_case",
        "singleword",
        "multiple___underscores",
        ""
    ]
    for case in test_cases:
        result = to_camel_case(case)
        print(result)