def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    samples = [
        "hello",
        "WORLD",
        "hElLo",
        "",
        "a",
        "123abc",
        "abc123"
    ]
    for sample in samples:
        print(capitalize_first(sample))