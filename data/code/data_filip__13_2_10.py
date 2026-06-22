def to_camel_case(text: str) -> str:
    if not text:
        return text
    
    leading_underscores = ""
    i = 0
    while i < len(text) and text[i] == "_":
        leading_underscores += "_"
        i += 1
    
    trailing_underscores = ""
    j = len(text) - 1
    while j >= i and text[j] == "_":
        trailing_underscores = "_" + trailing_underscores
        j -= 1
    
    core = text[i : j + 1] if j >= i else ""
    
    if not core:
        return leading_underscores + trailing_underscores
    
    parts = core.split("_")
    result_parts = []
    
    for idx, part in enumerate(parts):
        if not part:
            continue
        if idx == 0:
            result_parts.append(part)
        else:
            if part:
                result_parts.append(part[0].upper() + part[1:])
            else:
                result_parts.append("")
    
    camel_core = "".join(result_parts)
    return leading_underscores + camel_core + trailing_underscores

if __name__ == '__main__':
    samples = [
        "hello_world",
        "__leading_underscore",
        "trailing_underscore__",
        "___multiple___underscores___",
        "simple",
        "_single",
        "alreadyCamelCase",
        "snake_case_with_numbers_123",
        "multiple_consecutive___underscores_here"
    ]
    
    for s in samples:
        print(to_camel_case(s))