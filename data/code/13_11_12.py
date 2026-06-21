def to_camel_case(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    if not components:
        return ""
    first_component = components[0]
    if not first_component:
        return ""
    camel_str = first_component
    for component in components[1:]:
        if component:
            camel_str += component[0].upper() + component[1:]
    return camel_str

if __name__ == '__main__':
    sample_values = ['snake_case_example', 'this_is_a_test', 'a', '__double__underscore__', 'alreadyCamel', '']
    for value in sample_values:
        result = to_camel_case(value)
        print(f"{value!r} -> {result!r}")