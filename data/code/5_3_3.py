def capitalize_first_if_alphanumeric(s: str) -> str:
    if not s:
        return s
    first_char = s[0]
    if first_char.isalnum():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    examples = [
        "hello",
        "world",
        "123abc",
        "!test",
        "",
        " already capitalized",
        "python3"
    ]
    for example in examples:
        result = capitalize_first_if_alphanumeric(example)
        print(result)