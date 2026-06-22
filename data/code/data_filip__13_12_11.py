def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = ["hello_world", "snake_case_example", "this_is_a_test", "a", "alreadyCamel"]
    for case in test_cases:
        print(f"{case} -> {snake_to_camel(case)}")