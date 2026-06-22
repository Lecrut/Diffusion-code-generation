def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + "".join(s[1:])

if __name__ == '__main__':
    sample_string = "hello world"
    result = capitalize_first(sample_string)
    print(result)