def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_values = [
        "hello",
        "HELLO",
        "hELLO",
        "",
        "a",
        "abc123",
        "123abc",
        "python programming"
    ]
    for val in sample_values:
        print(capitalize_first(val))