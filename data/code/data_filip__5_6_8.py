def capitalize_first(s: str) -> str:
    if not s:
        return s
    first = s[0]
    rest = s[1:]
    if first.isascii():
        if first.islower():
            return first.upper() + rest
    else:
        upper = first.upper()
        if upper != first:
            return upper + rest
    return s

if __name__ == '__main__':
    test_strings = ["hello", "world", "a", "A", "", "café", "straße"]
    for s in test_strings:
        result = capitalize_first(s)
        print(result)