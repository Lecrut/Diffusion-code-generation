def capitalize_first_char(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_strings = ["hello world", "PyThOn", "tEsT", "A", "a", ""]
    for text in sample_strings:
        result = capitalize_first_char(text)
        print(result)