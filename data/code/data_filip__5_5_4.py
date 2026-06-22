def capitalize_first_letter(s: str) -> str:
    if not s:
        return s
    return s[:1].upper() + s[1:]

if __name__ == '__main__':
    sample_data = "hello world"
    result = capitalize_first_letter(sample_data)
    print(result)