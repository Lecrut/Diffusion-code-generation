def capitalize_first_if_alphanumeric(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.isalnum():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    examples = ["hello world", "123abc", "!hello", "", "Python", "9test", "$money", "a"]
    for text in examples:
        result = capitalize_first_if_alphanumeric(text)
        print(f"Input: {text!r} -> Output: {result!r}")