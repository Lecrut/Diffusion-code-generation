def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ""
    parts = snake_str.split("_")
    first = parts[0]
    rest = [part.capitalize() for part in parts[1:] if part]
    return first + "".join(rest)

if __name__ == "__main__":
    samples = [
        "hello_world",
        "snake_case_to_camel_case",
        "alreadyCamel",
        "single",
        "multiple___underscores",
        "",
        "a_b_c"
    ]
    for s in samples:
        print(snake_to_camel(s))