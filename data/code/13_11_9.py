def to_camel_case(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if not parts:
        return ""
    first_part = parts[0]
    if not first_part:
        return ""
    result = [first_part]
    for part in parts[1:]:
        if not part:
            result.append("")
            continue
        result.append(part[0].upper() + part[1:])
    return "".join(result)

if __name__ == '__main__':
    sample_inputs = ["my_variable_name", "hello_world", "_leading_underscore", "trailing_", "multiple___underscores", ""]
    results = []
    for s in sample_inputs:
        results.append(to_camel_case(s))
    for i, res in enumerate(results):
        print(f"{sample_inputs[i]} -> {res}")