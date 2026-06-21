def to_camel_case(snake_str):
    parts = snake_str.split('_')
    if not parts:
        return ""
    if not parts[0]:
        return "".join(word.capitalize() for word in parts[1:])
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_inputs = ["hello_world", "this_is_a_test", "snake_case_string", "single"]
    for s in sample_inputs:
        print(to_camel_case(s))