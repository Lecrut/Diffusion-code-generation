def to_camel_case(text):
    if not text:
        return text
    components = text.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "this_is_a_test_case",
        "single",
        "multiple___underscores",
        "alreadyCamelCase"
    ]
    for case in test_cases:
        result = to_camel_case(case)
        print(result)