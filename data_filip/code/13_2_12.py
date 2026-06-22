def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    
    parts = snake_str.split("_")
    result_parts = []
    
    for i, part in enumerate(parts):
        if part == "":
            continue
        if i == 0 and part:
            result_parts.append(part.lower())
        else:
            result_parts.append(part.capitalize())
    
    return "".join(result_parts)

if __name__ == "__main__":
    test_cases = [
        "snake_case",
        "alreadyCamel",
        "multiple___underscores",
        "_leading_underscore",
        "trailing_underscore_",
        "__double_leading",
        "double__trailing__",
        "a",
        "",
        "simple",
        "with_numbers_123_in_middle",
        "ALL_CAPS",
        "Mixed_Case_Input",
    ]
    
    for test in test_cases:
        print(f"{test!r} -> {snake_to_camel(test)!r}")