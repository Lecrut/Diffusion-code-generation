import re

def snake_to_camel(snake: str) -> str:
    if not snake:
        return ""

    is_leading_underscore = snake.startswith('_')
    if is_leading_underscore:
        snake = snake[1:]

    if not snake:
        return "_" if is_leading_underscore else ""

    result = []
    for part in snake.split('_'):
        if not part:
            continue
        if result:
            result.append(part[0].upper())
            result.append(part[1:])
        else:
            result.append(part)

    camel = "".join(result)
    if is_leading_underscore:
        return "_" + camel
    return camel

if __name__ == '__main__':
    samples = [
        "simple_case",
        "already_Camel",
        "__double_leading",
        "multiple___underscores",
        "single",
        "",
        "_",
        "__",
        "with__middle__underscores",
        "ends_with_",
        "UPPER_CASE_VAR",
    ]
    for sample in samples:
        print(snake_to_camel(sample))