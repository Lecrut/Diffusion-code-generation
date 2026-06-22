def to_camel_case(snake_str):
    if not snake_str:
        return snake_str
    leading_underscores = ""
    trailing_underscores = ""
    for char in snake_str:
        if char == "_":
            leading_underscores += char
        else:
            break
    for char in reversed(snake_str):
        if char == "_":
            trailing_underscores = char + trailing_underscores
        else:
            break
    core_part = snake_str[len(leading_underscores) : len(snake_str) - len(trailing_underscores)]
    if not core_part:
        return snake_str
    parts = core_part.split("_")
    camel_parts = [parts[0]]
    for part in parts[1:]:
        if not part:
            continue
        camel_parts.append(part.capitalize())
    result = "".join(camel_parts)
    return leading_underscores + result + trailing_underscores

if __name__ == '__main__':
    test_cases = [
        "example_string",
        "__leading_underscore",
        "trailing_underscore__",
        "__double__leading_and_trailing__",
        "multiple___consecutive___underscores",
        "single",
        "",
        "___",
        "alreadyCamelCase_not",
        "numbers_2_and_3_inside"
    ]
    for case in test_cases:
        print(f"{repr(case)} -> {repr(to_camel_case(case))}")