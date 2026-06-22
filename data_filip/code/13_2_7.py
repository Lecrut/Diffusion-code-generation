def snake_to_camel(s: str) -> str:
    if not s:
        return ""
    parts = s.split('_')
    filtered_parts = [p for p in parts if p]
    if not filtered_parts:
        return ""
    first = filtered_parts[0]
    rest = [p.capitalize() for p in filtered_parts[1:]]
    return first + ''.join(rest)

if __name__ == '__main__':
    samples = [
        "hello_world",
        "_leading_underscore",
        "trailing_underscore_",
        "__double__underscores__",
        "simple",
        "a_b_c",
        "",
        "_",
        "__",
        "alreadyCamel",
        "mixed_CASE_example"
    ]
    for sample in samples:
        print(f"{sample!r} -> {snake_to_camel(sample)!r}")